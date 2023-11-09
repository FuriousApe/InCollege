
import sqlite3
from data_ import connect_to_database

class Notification:

    def __init__(self, id, username, message, seen, menu):
        self.id = id
        self.username = username
        self.message = message
        self.seen = seen
        self.menu = menu

    @classmethod
    # Creates a new notification
    # Saves to database
    def create(cls, username, message, menu):

        connection, cursor = connect_to_database()
        if connection is None: return

        try:
            cursor.execute('''
                INSERT INTO notifications (username, message, seen, menu)
                VALUES (?, ?, ?, ?)
            ''', (username, message, False, menu))
            connection.commit()

        except sqlite3.Error as err:
            print("There was an error creating a notification:", err)
            return

        finally:
            if connection: connection.close()

    # Marks a notification as seen
    def seen(self):

        self.seen = True

        connection, cursor = connect_to_database()
        if connection is None: return

        try:
            cursor.execute('''
                UPDATE notifications
                SET seen = ?
                WHERE notification_id = ?
            ''', (True, self.id))
            connection.commit()

        except sqlite3.Error as err:
            print("There was an error marking the notification as 'seen':", err)
            return

        finally:
            if connection: connection.close()

    # Deletes a notification from the database
    def delete(self):

        connection, cursor = connect_to_database()
        if connection is None: return

        try:
            cursor.execute('''
                DELETE FROM notifications
                WHERE notification_id = ?
            ''', (self.id,))
            connection.commit()

        except sqlite3.Error as err:
            print("There was an error deleting the notification:", err)
            return

        finally:
            if connection: connection.close()

    @classmethod
    # Deletes all notifications for username
    # Erases from database
    def delete_all_for(cls, username, menu):

        connection, cursor = connect_to_database()
        if connection is None: return

        try:
            cursor.execute('''
                DELETE FROM notifications
                WHERE username = ? AND menu = ?
            ''', (username, menu))
            connection.commit()

        except sqlite3.Error as err:
            print("There was an error erasing the notifications:", err)
            return

        finally:
            if connection: connection.close()

    @classmethod
    # Retuns all notifications for the username
    # They return as objects
    def fetch_for(cls, username, menu):

        connection, cursor = connect_to_database()
        if connection is None: return []

        try:
            cursor.execute('''
                SELECT * FROM notifications
                WHERE username = ? AND menu = ?
            ''', (username, menu))
            notifications = cursor.fetchall()

            # Convert each row into a notification object, and return
            return [cls(id = row[0], username = row[1], message = row[2],
                        seen = row[3], menu = row[4]) for row in notifications]

        except sqlite3.Error as err:
            print("There was an error fetching notifications:", err)
            return []

        finally:
            if connection: connection.close()




# End of file
