
                       ###################################
############################                         ###########################
###########################  A P P L I C A T I O N S  ##########################
############################                         ###########################
                       ###################################

                  # All code pertaining to job applications. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3

import config
from config import DBApplications, DBJobs, DBSavedJobs
from data_ import connect_to

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Apply for Job                              #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                             #---------------------#
#----------------------------#    Apply for Job    #---------------------------#
                             #---------------------#

import sqlite3
import re

def apply_for_job(username, job_id):


    if is_own_job(username, job_id):
        print("You can't apply to your own job. That's called self-employment, and you don't need our services for that.")
        return


    # Validate date input
    def convert_to_sql_date(date_str):
        if re.match("^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$", date_str):
            month, day, year = date_str.split('/')
            return f"{year}-{month}-{day}"
        return None


    grad_date = input("Enter your graduation date (mm/dd/yyyy): ")
    sql_grad_date = convert_to_sql_date(grad_date)

    while sql_grad_date is None:
        print("Invalid date format. Please use mm/dd/yyyy.")
        grad_date = input("Enter your graduation date (mm/dd/yyyy): ")
        sql_grad_date = convert_to_sql_date(grad_date)


    start_date = input("Enter the date you can start working (mm/dd/yyyy): ")
    sql_start_date = convert_to_sql_date(start_date)

    while sql_start_date is None:
        print("Invalid date format. Please use mm/dd/yyyy.")
        start_date = input("Enter the date you can start working (mm/dd/yyyy): ")
        sql_start_date = convert_to_sql_date(start_date)


    app_text = input("Explain why you think you would be a good fit for this job: ")

    while len(app_text) < 10:
        print("Your explanation is too short. Please provide more details.")
        app_text = input("Explain why you think you would be a good fit for this job: ")

    connection, cursor = connect_to(DBApplications)
    if connection is None:
        return

    try:
        cursor.execute('''
            INSERT INTO applications (student_username, job_id, graduation_date, start_date, application_text)
            VALUES (?, ?, ?, ?, ?);
        ''', (username, job_id, sql_grad_date, sql_start_date, app_text))
        connection.commit()

    except sqlite3.Error as err:
        print("Error applying for the job: ", err)

    finally:
        if connection: connection.close()




                           #------------------------#
#--------------------------#    Check if Applied    #--------------------------#
                           #------------------------#

def has_already_applied(student_username, job_id):


    connection, cursor = connect_to(DBApplications)

    if connection is None:
        return False


    try:
        cursor.execute('''
            SELECT COUNT(*) FROM applications
            WHERE student_username = ? AND job_id = ?;
        ''', (student_username, job_id))

        count = cursor.fetchone()[0]

        return count > 0


    except sqlite3.Error as err:
        print("Error checking if already applied: ", err)
        return False


    finally:
        if connection: connection.close()



                     #------------------------------------#
#--------------------#    Check if Applicant is Poster    #--------------------#
                     #------------------------------------#


def is_own_job(student_username, job_id):

    connection, cursor = connect_to(DBJobs)
    if connection is None:
        return False

    try:
        cursor.execute('''
            SELECT COUNT(*) FROM jobs
            WHERE job_id = ? AND username = ?;
        ''', (job_id, student_username))

        count = cursor.fetchone()[0]
        return count > 0


    except sqlite3.Error as err:
        print("Error checking if own job: ", err)
        return False


    finally:
        if connection: connection.close()



                           #------------------------#
#--------------------------#    Get Applied Jobs    #--------------------------#
                           #------------------------#

def get_applied_jobs(student_username):

    # Connect to the 'applications' database
    connection_app, cursor_app = connect_to(DBApplications)
    if connection_app is None:
        return []

    try:
        # Attach the 'jobs' database
        cursor_app.execute("ATTACH DATABASE ? AS jobs", (DBJobs,))

        # Execute the query
        cursor_app.execute('''
            SELECT
                jobs.job_id,
                job_title,
                description,
                location,
                employer,
                salary,
                username
            FROM applications JOIN jobs
            WHERE jobs.job_id = applications.job_id
            AND applications.student_username = ?;
        ''', (student_username,))

        applied_jobs_data = cursor_app.fetchall()

        applied_jobs = [{
            "Id": job_id,
            "Job Title": job_title,
            "Description": description,
            "Location": location,
            "Employer": employer,
            "Salary": salary,
            "Username": username,
        } for job_id, job_title, description, location, employer, salary, username in applied_jobs_data]
        return applied_jobs

    except sqlite3.Error as err:
        print("Error fetching applied jobs: ", err)
        return []

    finally:
        if connection_app: connection_app.close()



                            #----------------------#
#---------------------------#    Get Saved Jobs    #---------------------------#
                            #----------------------#

def get_saved_jobs(student_username):

    # Connect to the 'saved jobs' database
    connection_saved, cursor_saved = connect_to(DBSavedJobs)
    if connection_saved is None:
        return []

    try:
        # Attach the 'jobs' database
        cursor_saved.execute("ATTACH DATABASE ? AS jobs", (DBJobs,))

        # Execute the query
        cursor_saved.execute('''
            SELECT
                jobs.job_id,
                job_title,
                description,
                location,
                employer,
                salary,
                username
            FROM jobs JOIN saved_jobs
            WHERE jobs.job_id = saved_jobs.job_id
            AND saved_jobs.student_username = ?;
        ''', (student_username,))

        saved_jobs_data = cursor_saved.fetchall()

        saved_jobs = [{
            "Id": job_id,
            "Job Title": job_title,
            "Description": description,
            "Location": location,
            "Employer": employer,
            "Salary": salary,
            "Username": username,
        } for job_id, job_title, description, location, employer, salary, username in saved_jobs_data]
        return saved_jobs

    except sqlite3.Error as err:
        print("Error fetching saved jobs: ", err)
        return []

    finally:
        if connection_saved: connection_saved.close()



                               #----------------#
#------------------------------#    Save Job    #------------------------------#
                               #----------------#


def save_job(student_username, job_id):

    connection, cursor = connect_to(DBSavedJobs)

    if connection is None:
        return

    try:
        cursor.execute('''
            INSERT INTO saved_jobs (student_username, job_id)
            VALUES (?, ?);
        ''', (student_username, job_id))
        connection.commit()


    except sqlite3.Error as err:

        print("Error saving job: ", err)


    finally:

        if connection: connection.close()



                              #------------------#
#-----------------------------#    Unsave Job    #-----------------------------#
                              #------------------#


def unsave_job(student_username, job_id):

    connection, cursor = connect_to(DBSavedJobs)

    if connection is None:
        return

    try:
        cursor.execute('''
            DELETE FROM saved_jobs
            WHERE student_username = ? AND job_id = ?;
        ''', (student_username, job_id))

        connection.commit()


    except sqlite3.Error as err:

        print("Error unmarking saved job: ", err)


    finally:

        if connection: connection.close()





# End of file
