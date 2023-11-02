
import sqlite3
from data_ import connect_to_database

import sqlite3

class Message:
    def __init__(self, sender, receiver, subject, body, is_read, message_id=None):
        self.message_id = message_id
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.is_read = is_read

    @classmethod
    def save(cls, sender, receiver, subject, body):
        connection, cursor = connect_to_database()

        if connection is None:
            return

        try:
            cursor.execute('''
                INSERT INTO messages (sender, receiver, subject, body, is_read)
                VALUES (?, ?, ?, ?, ?)
            ''', (sender, receiver, subject, body, False))
            connection.commit()

        except sqlite3.Error as err:
            print("There was an error saving the message: ", err)

        finally:
            if connection: connection.close()

    @classmethod
    def fetch_all(cls, username):
        connection, cursor = connect_to_database()

        if connection is None:
            return []

        try:
            cursor.execute('''
                SELECT message_id, sender, receiver, subject, body, is_read
                FROM messages
                WHERE receiver = ?
            ''', (username,))
            rows = cursor.fetchall()

            return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]

        except sqlite3.Error as err:
            print("Error fetching messages: ", err)
            return []

        finally:
            if connection: connection.close()

    def read(self):

        self.is_read = True
        connection, cursor = connect_to_database()

        if connection is None:
            return

        try:
            cursor.execute('''
                UPDATE messages
                SET is_read = ?
                WHERE message_id = ?
            ''', (True, self.message_id))
            connection.commit()

        except sqlite3.Error as err:
            print("Error updating message status: ", err)

        finally:
            if connection: connection.close()

    def delete(self):

        connection, cursor = connect_to_database()

        if connection is None:
            return

        try:
            cursor.execute('''
                DELETE FROM messages
                WHERE message_id = ?
            ''', (self.message_id,))
            connection.commit()

        except sqlite3.Error as err:
            print("Error deleting message: ", err)

        finally:
            if connection: connection.close()






# End of file
