
import sqlite3
from data_ import connect_to_database


class Application:
    def __init__(self, application_id, username, job_id, graduation_date, start_date, application_text, application_date):
        self.application_id = application_id
        self.username = username
        self.job_id = job_id
        self.graduation_date = graduation_date
        self.start_date = start_date
        self.application_text = application_text
        self.application_date = application_date

    @classmethod
    # Return all applications made by username
    def get_apps_from(cls, username):

        connection, cursor = connect_to_database()
        if connection is None: return []

        try:
            cursor.execute('''
                SELECT * FROM applications WHERE username = ?
            ''', (username,))
            application_rows = cursor.fetchall()

            # Convert each row into an Application object and return the list
            return [cls(application_id=row[0], username=row[1], job_id=row[2],
                        graduation_date=row[3], start_date=row[4],
                        application_text=row[5], application_date=row[6])
                        for row in application_rows]

        except sqlite3.Error as err:
            print("Error retrieving applications: ", err)
            return []

        finally:
            if connection: connection.close()




# End of file
