
import sqlite3
import config
from data_ import connect_to_database

from classes.UserSettings import UserSettings
from classes.UserProfile import UserProfile
from classes.Request import Request
from classes.Connection import Connection
from classes.Message import Message


class User:

    def __init__(self, username, password, first_name=None, last_name=None, university=None, major=None, created_a_profile=False, plus=False):

        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.university = university
        self.major = major
        self.created_a_profile = created_a_profile
        self.plus = plus
        self.friends = [friend[0] for friend in self.get_friends()]
        self.inbox = []

    def save(self):
        connection, cursor = connect_to_database()
        if connection is None: return

        try:
            cursor.execute('''
                SELECT username FROM users WHERE username = ?
            ''', (self.username,))
            user_exists = cursor.fetchone()

            if user_exists:
                # Update user's details
                cursor.execute('''
                    UPDATE users
                    SET password = ?, first_name = ?, last_name = ?, university = ?, major = ?, created_a_profile = ?, plus = ?
                    WHERE username = ?
                ''', (self.password, self.first_name, self.last_name, self.university, self.major, self.created_a_profile, self.plus, self.username))
            else:
                # Insert a new user
                cursor.execute('''
                    INSERT INTO users(username, password, first_name, last_name, university, major, created_a_profile, plus)
                    VALUES(?,?,?,?,?,?,?,?)
                ''', (self.username, self.password, self.first_name, self.last_name, self.university, self.major, self.created_a_profile, self.plus))

            connection.commit()

        except sqlite3.Error as err:
            print(f"There was an error saving '{self.username}' to the database: ", err)

        finally:
            if connection: connection.close()

    @classmethod
    def fetch(cls, username):

        connection, cursor = connect_to_database()
        if connection is None: return None

        try:
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user_data = cursor.fetchone()

            if user_data:
                return cls(*user_data)  # Creates a User object with the fetched data

        except sqlite3.Error as err:
            print(f"There was an error fetching '{username}' from the database: ", err)

        finally:
            if connection: connection.close()

        # To use:
        # current_user = User.fetch(username)

    @classmethod
    def username_exists(cls, username):

        connection, cursor = connect_to_database()
        if connection is None: return False  # Could also raise an exception

        try:
            cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
            user_data = cursor.fetchone()
            return bool(user_data)  # If user_data is not None, the username exists

        except sqlite3.Error as err:
            print(f"There was an error checking if the '{username}' username exists: ", err)

        finally:
            if connection: connection.close()

    @classmethod
    def create(cls, username, password, first_name=None, last_name=None, university=None, major=None, created_a_profile=False, plus=None):

        # At this point, the username is available
        new_user = cls(username, password, first_name, last_name, university, major, created_a_profile, plus)
        new_user.save()
        UserSettings.initialize_settings_for(username)
        UserProfile.initialize_profile_for(username, university, major)
        print(f"New user '{username}' has registered successfully.")
        return new_user

    @classmethod
    def validate_credentials(cls, username, password):

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            # Check for matching credentials in the database
            cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
            stored_password = cursor.fetchone()

            # If there's no such user or passwords don't match, return False
            if stored_password is None or stored_password[0] != password:
                return False

        except sqlite3.Error as err:
            print(f"There was an error validating login credentials for '{username}': ", err)
            return False

        finally:
            if connection: connection.close()

        return True

    @classmethod
    # Retrieve users based on certain attributes (case-insensitive)
    def get_users_by_attribute(cls, **kwargs):

        connection, cursor = connect_to_database()
        if connection is None: return []

        # Prepare the query based on kwargs
        search_terms = [f"lower({key}) LIKE lower(?)" for key in kwargs.keys()]
        search_query = " AND ".join(search_terms)
        search_values = tuple(kwargs.values())

        users = []

        try:
            # Fetch user data based on the provided attributes
            cursor.execute(f'''
                SELECT username, password, first_name, last_name, university, major, created_a_profile, plus
                FROM users
                WHERE {search_query}
            ''', search_values)

            for user_data in cursor.fetchall():
                user = cls(username=user_data[0], password=user_data[1],
                           first_name=user_data[2], last_name=user_data[3],
                           university=user_data[4], major=user_data[5],
                           created_a_profile=user_data[6], plus=user_data[7])
                users.append(user)

        except sqlite3.Error as err:
            print(f"Error retrieving users by attribute {kwargs}: ", err)
            return []

        finally:
            if connection: connection.close()

        return users


    def get_friends(self):

        connection, cursor = connect_to_database()
        if connection is None: return []

        try:
            # Find friendships where the user is user_id1 or user_id2
            cursor.execute('''
                SELECT person1, person2 FROM connections
                WHERE person1 = ? OR person2 = ?
            ''', (self.username, self.username))

            rows = cursor.fetchall()
            friend_usernames = []

            for row in rows:
                # Get the friend's username (the one that isn't this user's username)
                friend_usernames.append(row[0] if row[1] == self.username else row[1])

            # Fetch friend details from the users table
            placeholders = ', '.join('?' for _ in friend_usernames)
            cursor.execute(f'''
                SELECT username, created_a_profile FROM users
                WHERE username IN ({placeholders})
            ''', friend_usernames)

            friends = cursor.fetchall()
            return friends

        except sqlite3.Error as err:
            print(f"There was an error fetching friends for '{self.username}': ", err)

        finally:
            if connection: connection.close()

    @classmethod
    def has_room_for_new_account(cls):

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('SELECT COUNT(*) FROM users')
            current_user_count = cursor.fetchone()[0]

            if current_user_count < config.MaxAccounts:
                print("\n*\nGood news! We've got room for you!\n*\n")
                return True
            else:
                print("\n*\nAll permitted accounts have been created, please come back later.\n*\n")
                return False

        except sqlite3.Error as err:
            print("There was an error fetching the user count: ", err)
            return False

        finally:
            if connection: connection.close()


    #::::::::::::::::::::::::::  S E T T I N G S

    def get_settings(self):
        return UserSettings.fetch(self.username)

    def update_settings(self, **settings):
        return UserSettings.save(self.username, **settings)

    def toggle_setting(self, setting):
        return UserSettings.toggle_setting_for(self.username, setting)

    def toggle_language(self):
        return UserSettings.toggle_language_for(self.username)


    #::::::::::::::::::::::::::  P R O F I L E S

    def get_profile(self):
        return UserProfile.fetch(self.username)

    def update_profile(self, **profile_data):
        profile = self.get_profile()
        for key, value in profile_data.items():
            setattr(profile, key, value)
        return profile.save()


    #::::::::::::::::::::::::::  R E Q U E S T S

    def send_request(self, recipient_username):
        request = Request(None, self.username, recipient_username)
        return request.send()

    def accept_request(self, requester):
        request = self.get_request_of(requester) # Get request object
        if request:
            self.add_friend(requester) # Add both users to each other's friend list
            self.save() # Save both users to database
            requester.save()
            return request.delete() # Delete the request
        return False

    def reject_request(self, requester):
        request = self.get_request_of(requester)
        if request:
            return request.delete()
        return False

    def pending_requests(self):
        return Request.get_pending_requests(self.username)

    def get_request_of(self, requester):
        requests = self.pending_requests()
        for request in requests:
            if request.requester == requester.username:
                return request
        return None


    #::::::::::::::::::::::::::  C O N N E C T I O N S

    # Saves connection to database
    def add_connection(self, other_username):
        connection = Connection(None, self.username, other_username)
        return connection.save()

    # Deletes connection from database
    def remove_connection(self, other_username):
        connections = self.get_all_connections()
        for conn in connections:
            if conn.person1 == other_username or conn.person2 == other_username:
                return conn.delete()
        return False

    # Returns all connections of self
    def get_all_connections(self):
        return Connection.get_all(self.username)


    #::::::::::::::::::::::::::  N O T I F I C A T I O N S

    # Fetches all notifications for self
    def fetch_notifications(self):
        connection, cursor = connect_to_database()
        if connection is None: return []

        try:
            cursor.execute('SELECT message FROM notifications WHERE username = ?', (self.username,))
            return [row[0] for row in cursor.fetchall()]

        except sqlite3.Error as err:
            print(f"Error fetching notifications for {self.username}: ", err)
            return []

        finally:
            if connection: connection.close()

    # Deletes all notifications for self
    def delete_notifications(self):
        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('DELETE FROM notifications WHERE username = ?', (self.username,))
            connection.commit()
            return True

        except sqlite3.Error as err:
            print(f"Error deleting notifications for {self.username}: ", err)
            return False

        finally:
            if connection: connection.close()


    #::::::::::::::::::::::::::  M A I L  &  M E S S A G E S

    # Takes object and 2 strings, sends message
    def send_message(self, target, subject, content):
        Message.save(self.username, target.username, subject, content)

    # Takes object, returns bool for friendship status
    def is_friend_of(self, other_user):
        return other_user.username in self.friends

    # Displays user's inbox
    def view_inbox(self):
        self.inbox = Message.fetch_all(self.username)
        if not self.inbox:
            print("               Your inbox is empty.              ")
            return

        for index, message in enumerate(self.inbox, start=1):
            status = "*" if message.is_read == False else " "
            print(f" {status} [{index}] From: {message.sender} | Subject: {message.subject}")

    # Takes object, formats & displays it
    def read_message(self, message):
        print(f"\nFrom: {message.sender}")
        print(f"Subject: {message.subject}")
        print("----------------------")
        print(message.body)
        print("----------------------\n")
        message.read()
        choice = input("Do you want to delete this message? (Y/N) ").upper()
        if choice == "Y":
            message.delete()
            self.inbox.remove(message)
            print("\nMessage deleted.\n")

    # Takes object, connects self and friend
    def add_friend(self, friend):
        if not self.is_friend_of(friend):
            self.add_connection(friend.username)
            self.friends = [friend[0] for friend in self.get_friends()]
            friend.friends = [user[0] for user in friend.get_friends()]

    # Prints usernames of friend list
    def view_friends(self):
        if not self.friends:
            print("You have no friends added.")
            return
        for index, friend in enumerate(self.friends, start=1):
            print(f"{index}. {friend}")

    @classmethod
    # Returns all usernames in alphabetical order
    def all_usernames(cls):

        connection, cursor = connect_to_database()
        if connection is None: return []

        try:
            cursor.execute("SELECT username FROM users ORDER BY username ASC")
            usernames = cursor.fetchall()
            # Extract usernames from the tuples returned by fetchall
            return [username[0] for username in usernames]

        except sqlite3.Error as error:
            print("Error while fetching usernames: ", error)
            return []

        finally:
            if connection: connection.close()


    # Notifies of unread message(s)
    def receive_notifications(self):
        unread_msgs = [msg for msg in self.inbox if msg.is_read == False]
        if unread_msgs:
            print("\n|::::::::::::::::::::::::::::::::::::::::::::::::")
            print(f"  You have {len(unread_msgs)} unread messages!")
            print("|::::::::::::::::::::::::::::::::::::::::::::::::\n")


# End of file