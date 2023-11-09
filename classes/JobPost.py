
import sqlite3
from datetime import datetime
from data_ import connect_to_database
from classes.Application import Application


class JobPost:

    def __init__(self, job_id=None, job_title=None, description=None, location=None, employer=None, salary=None, username=None, date_posted=None):
        self.job_id = job_id
        self.job_title = job_title
        self.description = description
        self.location = location
        self.employer = employer
        self.salary = salary
        self.username = username
        self.date_posted = date_posted

    # Save a job object to the database
    def post(self):

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            if self.job_id:
                # Update an existing job post
                cursor.execute('''
                    UPDATE jobs SET
                    job_title = ?,
                    description = ?,
                    location = ?,
                    employer = ?,
                    salary = ?,
                    username = ?
                    date_posted = ?
                    WHERE job_id = ?
                ''', (self.job_title, self.description, self.location, self.employer, self.salary, self.username, self.date_posted, self.job_id))
            else:
                # Insert a new job post
                cursor.execute('''
                    INSERT INTO jobs (job_title, description, location, employer, salary, username, date_posted)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (self.job_title, self.description, self.location, self.employer, self.salary, self.username, self.date_posted))
                self.job_id = cursor.lastrowid

            connection.commit()
            return True

        except sqlite3.Error as err:
            print(f"Error saving job post: ", err)
            return False

        finally:
            if connection: connection.close()

    @classmethod
    # Return specific job post as object
    def fetch(cls, job_id):

        connection, cursor = connect_to_database()
        if connection is None: return None

        try:
            cursor.execute('''
                SELECT * FROM jobs WHERE job_id = ?
            ''', (job_id,))
            data = cursor.fetchone()
            if data:
                return cls(job_id=data[0], job_title=data[1],
                           description=data[2], location=data[3],
                           employer=data[4], salary=data[5],
                           username=data[6], date_posted=data[7])

        except sqlite3.Error as err:
            print(f"Error retrieving job post with ID {job_id}: ", err)

        finally:
            if connection: connection.close()

        return None

    @classmethod
    # Return all job posts as objects
    def fetch_all(cls):

        connection, cursor = connect_to_database()
        if connection is None: return []

        try:
            cursor.execute('SELECT * FROM jobs')
            data = cursor.fetchall()
            return [cls(job_id=row[0], job_title=row[1],
                        description=row[2], location=row[3],
                        employer=row[4], salary=row[5],
                        username=row[6], date_posted=row[7]) for row in data]

        except sqlite3.Error as err:
            print(f"Error retrieving all job posts: ", err)

        finally:
            if connection: connection.close()

        return []

    # Delete a specific job from the database
    def delete(self, username):

        if not self.job_id: return False

        if self.username != username:
            print("Error: Only the user who posted the job can delete it.")
            return False

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('DELETE FROM jobs WHERE job_id = ?', (self.job_id,))
            connection.commit()

            # Notify users after successfully deleting the job post
            self.notify_users_about_deletion(self.job_id, f"A job you saved or applied for has been deleted: {self.job_title}")

            return True

        except sqlite3.Error as err:
            print(f"Error deleting job post with ID {self.job_id}: ", err)
            return False

        finally:
            if connection: connection.close()

    @staticmethod
    # Notifies users who have saved or applied to the job about its deletion
    def notify_users_about_deletion(job_id, message):

        connection, cursor = connect_to_database()
        if connection is None: return

        try:
            # Fetch users who saved or applied to the job
            cursor.execute('''
                SELECT DISTINCT username
                FROM (
                    SELECT username FROM saved_jobs WHERE job_id = ?
                    UNION
                    SELECT username FROM applications WHERE job_id = ?
                )
            ''', (job_id, job_id))

            users_to_notify = [row[0] for row in cursor.fetchall()]

            # Insert notifications for these users
            for user in users_to_notify:
                cursor.execute('''
                    INSERT INTO notifications (username, message, menu)
                    VALUES (?, ?)
                ''', (user, message, 'job'))

            connection.commit()

        except sqlite3.Error as err:
            print(f"Error notifying users about job deletion: {err}")

        finally:
            if connection: connection.close()

    # Allows user to make it a 'Saved Job'
    def save(self, username):

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('''
                INSERT INTO saved_jobs (username, job_id)
                VALUES (?, ?)
            ''', (username, self.job_id))
            connection.commit()
            return True

        except sqlite3.IntegrityError:
            print(f"Job with ID {self.job_id} is already saved by user {username}.")
            return False

        except sqlite3.Error as err:
            print("Error saving the job: ", err)
            return False

        finally:
            if connection: connection.close()

    # Allows user to unsave it from Saved Jobs
    def unsave(self, username):

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('''
                DELETE FROM saved_jobs WHERE username = ? AND job_id = ?
            ''', (username, self.job_id))
            connection.commit()
            return True

        except sqlite3.Error as err:
            print("Error removing the saved job: ", err)
            return False

        finally:
            if connection: connection.close()

    # Check if job is saved by username
    def is_saved_by(self, username):

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('''
                SELECT 1 FROM saved_jobs WHERE username = ? AND job_id = ?
            ''', (username, self.job_id))
            return bool(cursor.fetchone())

        except sqlite3.Error as err:
            print("Error checking if job is saved: ", err)
            return False

        finally:
            if connection: connection.close()

    @classmethod
    # Return all saved jobs for a user
    def get_saved_jobs(cls, username):

        connection, cursor = connect_to_database()
        if connection is None: return []

        try:
            # First, get the job_ids of saved jobs for this user
            cursor.execute('''
                SELECT job_id FROM saved_jobs WHERE username = ?
            ''', (username,))
            saved_job_ids = [row[0] for row in cursor.fetchall()]

            if not saved_job_ids: return []

            # Then, get the info of each job
            jobs_query = f'''
                SELECT * FROM jobs WHERE job_id IN ({','.join(['?'] * len(saved_job_ids))})
            '''
            cursor.execute(jobs_query, saved_job_ids)
            job_rows = cursor.fetchall()

            # Convert each row into a JobPost object, return the list
            return [cls(job_id=row[0], job_title=row[1], description=row[2], location=row[3], employer=row[4],
                        salary=row[5], username=row[6], date_posted=row[7]) for row in job_rows]

        except sqlite3.Error as err:
            print("Error retrieving saved jobs: ", err)
            return []

        finally:
            if connection: connection.close()

    # Allows a user to save an application for a specific job
    def apply(self, username, graduation_date, start_date, application_text):

        today = datetime.now()

        connection, cursor = connect_to_database()
        if connection is None: return None

        try:
            cursor.execute('''
                INSERT INTO applications (username, job_id, graduation_date, start_date, application_text, application_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (username, self.job_id, graduation_date, start_date, application_text, today))
            connection.commit()

            return Application(application_id=cursor.lastrowid, username=username, job_id=self.job_id,
                       graduation_date=graduation_date, start_date=start_date,
                       application_text=application_text, application_date=today)

        except sqlite3.Error as err:
            print("Error applying for the job: ", err)
            return None

        finally:
            if connection: connection.close()

    # Checks if username has already applied
    def has_applied(self, username):

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('''
                SELECT COUNT(*)
                FROM applications
                WHERE username = ? AND job_id = ?
            ''', (username, self.job_id))

            count = cursor.fetchone()[0]
            return count > 0

        except sqlite3.Error as err:
            print(f"Error checking application for username {username}: ", err)
            return False

        finally:
            if connection: connection.close()

    @classmethod
    def get_applied_jobs(cls, username):

        connection, cursor = connect_to_database()
        if connection is None: return []

        try:
            # Get the job_ids of jobs the user has applied for
            cursor.execute('''
                SELECT job_id FROM applications WHERE username = ?
            ''', (username,))
            applied_job_ids = [row[0] for row in cursor.fetchall()]

            if not applied_job_ids: return []

            # Get the info of each job
            jobs_query = f'''
                SELECT * FROM jobs WHERE job_id IN ({','.join(['?'] * len(applied_job_ids))})
            '''
            cursor.execute(jobs_query, applied_job_ids)
            job_rows = cursor.fetchall()

            # Convert each row into an object, return the list
            return [cls(job_id=row[0], job_title=row[1], description=row[2], location=row[3], employer=row[4],
                        salary=row[5], username=row[6], date_posted=row[7]) for row in job_rows]

        except sqlite3.Error as err:
            print(f"Error fetching applied jobs for username {username}: ", err)
            return []

        finally:
            if connection: connection.close()




# End of file
