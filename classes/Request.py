
import sqlite3
from data_ import connect_to_database


class Request:

    def __init__(self, request_id, requester, recipient):
        self.request_id = request_id
        self.requester = requester
        self.recipient = recipient

    def send(self):
        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('''
                INSERT INTO requests (requester, recipient)
                VALUES (?, ?);
            ''', (self.requester, self.recipient))
            connection.commit()
            self.request_id = cursor.lastrowid  # get the last inserted id
            return True

        except sqlite3.Error as err:
            print("Error sending friend request: ", err)
            return False

        finally:
            if connection: connection.close()

    def delete(self):

        if not self.request_id: return False

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('DELETE FROM requests WHERE request_id = ?', (self.request_id,))
            connection.commit()
            return True

        except sqlite3.Error as err:
            print("Error rejecting friend request: ", err)
            return False

        finally:
            if connection: connection.close()

    @staticmethod
    def get_pending_requests(username):

        connection, cursor = connect_to_database()
        if connection is None: return []

        try:
            cursor.execute('SELECT request_id, requester FROM requests WHERE recipient = ?', (username,))
            return [Request(row[0], row[1], username) for row in cursor.fetchall()]

        except sqlite3.Error as err:
            print("Error fetching pending requests: ", err)
            return []

        finally:
            if connection: connection.close()




# End of file
