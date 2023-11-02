import sqlite3
from data_ import connect_to_database

class UserProfile:

    class Job:
        def __init__(self, title, employer, date_started, date_ended, location, description):
            self.title = title
            self.employer = employer
            self.date_started = date_started
            self.date_ended = date_ended
            self.location = location
            self.description = description

    def __init__(self, username, title, about, jobs, university, major, years_attended):
        self.username = username
        self.title = title
        self.about = about
        self.jobs = jobs  # This is going to be a list of Job objects
        self.university = university
        self.major = major
        self.years_attended = years_attended

    @classmethod
    def fetch(cls, username):

        connection, cursor = connect_to_database()
        if connection is None: return None

        try:
            cursor.execute('''
                SELECT * FROM profiles WHERE username = ?
            ''', (username,))
            data = cursor.fetchone()
            if data:
                jobs = [
                    cls.Job(data[3], data[4], data[5], data[6], data[7], data[8]),
                    cls.Job(data[9], data[10], data[11], data[12], data[13], data[14]),
                    cls.Job(data[15], data[16], data[17], data[18], data[19], data[20])
                ]
                return cls(username=data[0], title=data[1], about=data[2], jobs=jobs,
                           university=data[21], major=data[22], years_attended=data[23])

        except sqlite3.Error as err:
            print(f"Error retrieving profile for {username}: ", err)

        finally:
            if connection: connection.close()

        return None

    def save(self):

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('''
                UPDATE profiles SET
                title = ?,
                about = ?,

                job_1_title = ?,
                job_1_employer = ?,
                job_1_date_started = ?,
                job_1_date_ended = ?,
                job_1_location = ?,
                job_1_description = ?,

                job_2_title = ?,
                job_2_employer = ?,
                job_2_date_started = ?,
                job_2_date_ended = ?,
                job_2_location = ?,
                job_2_description = ?,

                job_3_title = ?,
                job_3_employer = ?,
                job_3_date_started = ?,
                job_3_date_ended = ?,
                job_3_location = ?,
                job_3_description = ?,

                university = ?,
                major = ?,
                years_attended = ?

                WHERE username = ?
            ''', (
                self.title,
                self.about,

                self.jobs[0].title,
                self.jobs[0].employer,
                self.jobs[0].date_started,
                self.jobs[0].date_ended,
                self.jobs[0].location,
                self.jobs[0].description,

                self.jobs[1].title if len(self.jobs) > 1 else None,
                self.jobs[1].employer if len(self.jobs) > 1 else None,
                self.jobs[1].date_started if len(self.jobs) > 1 else None,
                self.jobs[1].date_ended if len(self.jobs) > 1 else None,
                self.jobs[1].location if len(self.jobs) > 1 else None,
                self.jobs[1].description if len(self.jobs) > 1 else None,

                self.jobs[2].title if len(self.jobs) > 2 else None,
                self.jobs[2].employer if len(self.jobs) > 2 else None,
                self.jobs[2].date_started if len(self.jobs) > 2 else None,
                self.jobs[2].date_ended if len(self.jobs) > 2 else None,
                self.jobs[2].location if len(self.jobs) > 2 else None,
                self.jobs[2].description if len(self.jobs) > 2 else None,

                self.university,
                self.major,
                self.years_attended,

                self.username
            ))
            connection.commit()
            return True

        except sqlite3.Error as err:
            print(f"There was an error updating profile for {self.username}: ", err)
            return False

        finally:
            if connection: connection.close()

    @classmethod
    def initialize_profile_for(cls, username, university, major):

        connection, cursor = connect_to_database()
        if connection is None: return False

        # Default values for all the other attributes
        default_title = ""
        default_about = ""
        default_jobs = [("","","","","","") for _ in range(3)]
        default_years_attended = ""

        try:
            cursor.execute('''
                INSERT INTO profiles (
                    username, title, about,
                    job_1_title, job_1_employer, job_1_date_started, job_1_date_ended, job_1_location, job_1_description,
                    job_2_title, job_2_employer, job_2_date_started, job_2_date_ended, job_2_location, job_2_description,
                    job_3_title, job_3_employer, job_3_date_started, job_3_date_ended, job_3_location, job_3_description,
                    university, major, years_attended
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (username, default_title, default_about, *default_jobs[0], *default_jobs[1], *default_jobs[2], university, major, default_years_attended))
            connection.commit()

        except sqlite3.Error as err:
            print(f"There was an error initializing the profile for '{username}': ", err)
            return False

        finally:
            if connection: connection.close()

        return True





# End of file
