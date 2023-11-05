
import sqlite3
from data_ import connect_to_database


class Connection:

    def __init__(self, connection_id, person1, person2):
        self.connection_id = connection_id
        self.person1 = person1
        self.person2 = person2

    def save(self):
        connection, cursor = connect_to_database()
        if connection is None:
            return False

        try:
            cursor.execute('''
                INSERT INTO connections (person1, person2)
                VALUES (?, ?);
            ''', (self.person1, self.person2))
            connection.commit()
            self.connection_id = cursor.lastrowid
            return True

        except sqlite3.Error as err:
            print("Error creating connection: ", err)
            return False

        finally:
            if connection: connection.close()

    def delete(self):
        if not self.connection_id:
            return False

        connection, cursor = connect_to_database()
        if connection is None:
            return False

        try:
            cursor.execute('DELETE FROM connections WHERE connection_id = ?', (self.connection_id,))
            connection.commit()
            return True

        except sqlite3.Error as err:
            print("Error deleting connection: ", err)
            return False

        finally:
            if connection: connection.close()

    @staticmethod
    def get(connection_id):
        connection, cursor = connect_to_database()
        if connection is None:
            return None

        try:
            cursor.execute('SELECT person1, person2 FROM connections WHERE connection_id = ?', (connection_id,))
            row = cursor.fetchone()
            if row:
                return Connection(connection_id, row[0], row[1])
            return None

        except sqlite3.Error as err:
            print("Error fetching connection: ", err)
            return None

        finally:
            if connection: connection.close()

    @staticmethod
    def get_all(username):
        connection, cursor = connect_to_database()
        if connection is None:
            return []

        try:
            cursor.execute('''
                SELECT connection_id, person1, person2
                FROM connections
                WHERE person1 = ? OR person2 = ?;
            ''', (username, username))
            return [Connection(row[0], row[1], row[2]) for row in cursor.fetchall()]

        except sqlite3.Error as err:
            print("Error fetching all connections for user: ", err)
            return []

        finally:
            if connection: connection.close()






# End of file
