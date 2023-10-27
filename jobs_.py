
                              #####################
###################################           ##################################
###################################  J O B S  ##################################
###################################           ##################################
                              #####################

                         # All code pertaining to jobs. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3

import config

import home_
import applications_
from config import DBJobs, DBApplications
from data_ import connect_to

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Parse Salary                               #
#                             [ 2 ] Load Jobs                                  #
#                             [ 3 ] Count Jobs                                 #
#                             [ 4 ] Post Job                                   #
#                             [ 5 ] Upload Job                                 #
#                             [ 6 ] Delete Job                                 #
#                             [ 7 ] Job Menu                                   #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                             #--------------------#
#----------------------------#    Parse Salary    #----------------------------#
                             #--------------------#

           # Removes any unwanted characters that may have been input #
                   # Called towards beginning of post_job() #

def parse_salary():

    while True:

# Prompt

        salary = input("  Salary: ")


# Replace Unwanted Characters

        salary = salary.replace('$', '')
        salary = salary.replace(',', '')

        if salary.replace('.', '').isdigit(): break


# Error Handling

        else:
            print("Invalid salary - please input only numeric values.")

    return float(salary)

                             #---------------------#
#----------------------------#      Load Jobs      #---------------------------#
                             #---------------------#

            # Gets all jobs from job posting database, returns them. #
                             # Called in count jobs #

def load_jobs():


# Connect to Database

    connection, cursor = connect_to(DBJobs)

    if connection is None:
        return


# Define Target Info

    query = '''
        SELECT
            job_id,
            job_title,
            description,
            location,
            employer,
            salary,
            first_name,
            last_name
        FROM
            jobs;
    '''


# Execute Query

    try:
        cursor.execute(query)
        jobs_data = cursor.fetchall()
        config.Jobs = [{
            "Id": job_id,
            "Job Title": job_title,
            "Description": description,
            "Location": location,
            "Employer": employer,
            "Salary": salary,
            "First Name": first_name,
            "Last Name": last_name
        } for job_id, job_title, description, location, employer, salary, first_name, last_name in jobs_data]

    except sqlite3.Error as err:
        print("There was an error delivering the query: ", err)


# Close Connection

    finally:

        if connection:
            connection.commit()
            connection.close()

            return config.Jobs



                              #------------------#
#-----------------------------#    Count Jobs    #-----------------------------#
                              #------------------#

  # Counts number of jobs in database, returns True if there's room for more #
                     # Called at beginning of post_job() #

def room_for_job():

    jobs = load_jobs()

    if jobs:
        job_count = len(jobs)
        return job_count < config.MaxJobs

    else: return True

                               #----------------#
#------------------------------#    Post Job    #------------------------------#
                               #----------------#

         # Gets information about job from user, saves it to database #
                       # One of the options in job_menu() #

def post_job(first_name, last_name):


    print("")
    print("|----------------------------|")
    print("          Post a Job          ")
    print("|----------------------------|")
    print("")

    if room_for_job():

# Collect Info

        job_title = input("  Job Title: ")
        description = input("  Description: ")
        location = input("  Location: ")
        employer = input("  Employer: ")
        salary = parse_salary()


# Store in Dict

        job = {
            "Job Title": job_title,
            "Description": description,
            "Location": location,
            "Employer": employer,
            "Salary": salary,
            "First Name": first_name,
            "Last Name": last_name
        }


# Save to DB

        upload_job(job)
        config.Jobs = load_jobs()
        print("Your job has been posted!")


# If Database is Full

    else:
        print("")
        print("We're sorry. Our 'Jobs' database is currently full.")
        print("Please return later when there is room for another posting.")
        print("")
        print("Have a nice day.")



                              #------------------#
#-----------------------------#    Upload Job    #-----------------------------#
                              #------------------#

          # Takes a dict of job info, uploads it to the job database #
                   # Called during the post_job() function #

def upload_job(job):


# Connect to DB

    connection, cursor = connect_to(DBJobs)


# To these Columns...

    query = '''
        INSERT INTO jobs (
            job_title,
            description,
            location,
            employer,
            salary,
            first_name,
            last_name
        )
        VALUES (?, ?, ?, ?, ?, ?, ?);
        '''


# ...Insert this Data from Argument

    try:
        cursor.execute(query,
            (
                job["Job Title"],
                job["Description"],
                job["Location"],
                job["Employer"],
                job["Salary"],
                job["First Name"],
                job["Last Name"]
            )
        )

        connection.commit()
        print("Job posting saved!")


# Error Handling

    except sqlite3.Error as err:
        print("There was an error saving the job: ", err)


# Close Connection

    finally: connection.close()







                              #------------------#
#-----------------------------#    Delete Job    #-----------------------------#
                              #------------------#

                  # Deletes a job posting from the database #
                  # Must pass job poster's name as argument #


def delete_job(job_id, job_poster_username):

    # Connect to the 'jobs' database
    connection_jobs, cursor_jobs = connect_to(DBJobs)
    if connection_jobs is None:
        return

    try:
        # Attach the 'applications' database
        cursor_jobs.execute("ATTACH DATABASE ? AS apps_db", (DBApplications,))

        # Check if the job belongs to the poster
        cursor_jobs.execute('''
            SELECT COUNT(*) FROM jobs
            WHERE job_id = ? AND (first_name, last_name) = (
                SELECT first_name, last_name FROM accounts WHERE username = ?
            );
        ''', (job_id, job_poster_username))

        count = cursor_jobs.fetchone()[0]

        if count == 0:
            print("You are not authorized to delete this job.")
            return

        # Delete the job from the 'jobs' table
        cursor_jobs.execute('''
            DELETE FROM jobs
            WHERE job_id = ?;
        ''', (job_id,))

        # Remove application notifications from the 'applications' database
        cursor_jobs.execute('''
            DELETE FROM apps_db.applications
            WHERE job_id = ?;
        ''', (job_id,))

        connection_jobs.commit()

        # Update the job list in your configuration
        config.Jobs = []
        config.Jobs = load_jobs()


    except sqlite3.Error as err:
        print("Error deleting job: ", err)


    finally:
        if connection_jobs: connection_jobs.close()





                              #------------------#
#-----------------------------#    Search Job    #-----------------------------#
                              #------------------#

        # Searches the database for a job posted by a certain person #
                    # Returns a Bool based on existence #


def search_job(title, poster_first_name, poster_last_name):


# Connect to DB

    connection, cursor = connect_to(DBJobs)


# Query Definition

    query = '''
        SELECT
            job_title,
            first_name,
            last_name
        FROM
            jobs
        WHERE
            job_title = ?
            AND
            first_name = ?
            AND
            last_name = ?;
        '''


# Query Execution

    try:
        cursor.execute(query,
            (
                title,
                poster_first_name,
                poster_last_name
            )
        )

        job_data = cursor.fetchone()
        job_posting = [
                        {
                        "Job Title": job_title,
                        "Poster First Name": first_name,
                        "Poster Last Name": last_name
                        }
                        for job_title, first_name, last_name in job_data
                      ]

        job_found = job_posting["Job Title"] == title

        if job_found: return True
        else: return False

    except sqlite3.Error as err:
        print("There was an error searching for the job in the database: ", err)


# Close Connection

    finally:
        if connection: connection.commit(); connection.close()





                         #-----------------------------#
#------------------------#    Deletion Notification    #-----------------------#
                         #-----------------------------#


def notify_job_deletions_since_last_visit(username):

    # Connect to the 'applications' database
    connection_app, cursor_app = connect_to(DBApplications)
    if connection_app is None:
        return

    try:
        # Attach the 'jobs' database
        cursor_app.execute("ATTACH DATABASE ? AS jobs_db", (DBJobs,))

        # Fetch the titles of jobs the student had previously applied for
        cursor_app.execute('''
            SELECT jobs_db.jobs.job_title FROM applications
            INNER JOIN jobs_db.jobs ON applications.job_id = jobs_db.jobs.job_id
            WHERE applications.student_username = ?;
        ''', (username,))

        previous_applied_job_titles = [row[0] for row in cursor_app.fetchall()]

        # Fetch current job titles from the 'jobs' database
        cursor_app.execute('SELECT job_title FROM jobs_db.jobs;')
        current_job_titles = [row[0] for row in cursor_app.fetchall()]

        # Determine which previously applied-for jobs have been deleted
        deleted_job_titles = set(previous_applied_job_titles) - set(current_job_titles)

        if deleted_job_titles:
            print("We're sorry. Jobs you applied for have been deleted since your last visit.")
            for job_title in deleted_job_titles:
                print(f"The job '{job_title}' has been deleted.")


    except sqlite3.Error as err:
        print("Error notifying about job deletions: ", err)


    finally:
        if connection_app: connection_app.close()





#------------------------------#----------------#------------------------------#
#------------------------------#    Job Menu    #------------------------------#
#------------------------------#----------------#------------------------------#

       # Provides option to find a job, find an internship, or post a job #
                      # One of the paths from home() #

def job_menu():

    config.Jobs = load_jobs()

    while True:


        print("")
        print("|-----------------------------|")
        print("    Job Search / Internship    ")
        print("|-----------------------------|")
        print("")

        # Options
        print("  [1] Find a Job")
        print("   [2] Find an Internship")
        print("    [3] Post a Job")
        print("     [4] Saved Jobs")
        print("      [5] Return")
        print("")

        jobs_choice = input("Enter an option (or press Enter to access links): ")
        print("")

        # Outcomes
        if jobs_choice == "": home_.linkster()
        elif jobs_choice == "1": find_job()
        elif jobs_choice == "2": config.under_construction()
        elif jobs_choice == "3": post_job(config.User["First Name"], config.User["Last Name"])
        elif jobs_choice == "4": saved_jobs_menu()
        elif jobs_choice == "5": return

        else:
            print("Invalid choice. Please enter an available option.")




#---------------------------#-----------------------#--------------------------#
#---------------------------#    Saved Jobs Menu    #--------------------------#
#---------------------------#-----------------------#--------------------------#

def saved_jobs_menu():

    while True:

        print("")
        print("|-------------------------|")
        print("        Saved Jobs         ")
        print("|-------------------------|")
        print("")

        saved_jobs = applications_.get_saved_jobs(config.User["Username"])

        if not saved_jobs:
            print("No saved jobs found.")
            return

        # Get saved job titles and IDs
        saved_job_titles = [job['Job Title'] for job in saved_jobs]
        saved_job_ids = [job['Job ID'] for job in saved_jobs]

        # Display titles
        for index, job_title in enumerate(saved_job_titles, start=1):
            print(f"  [{index}] {job_title}")

        print("  [<] Return")
        print("")

        saved_jobs_choice = input("Enter an option (or press Enter to access links): ")
        print("")

        if saved_jobs_choice == "": home_.linkster()
        elif saved_jobs_choice == "<": return

        elif saved_jobs_choice.isdigit():
            selected_index = int(saved_jobs_choice) - 1
            if 0 <= selected_index < len(saved_job_titles):
                selected_job_title = saved_job_titles[selected_index]
                selected_job_id = saved_job_ids[selected_index]
                display_job_details(selected_job_title, selected_job_id)
            else:
                print("Invalid choice. Please select an available option.")

        else: print("Invalid choice. Please select an available option.")




                          #---------------------------#
#-------------------------#    Display Job Details    #------------------------#
                          #---------------------------#

def display_job_details(job_title, job_id):

    username = config.User["Username"]

    for job in config.Jobs:
        if job["Id"] == job_id:
            job_details = job

    if job_details:

        print(f"Job Title: {job_title}")
        print(f"Description: {job_details['Description']}")
        print(f"Location: {job_details['Location']}")
        print(f"Employer: {job_details['Employer']}")
        print(f"Salary: {job_details['Salary']}")
        print("")


        saved_jobs = applications_.get_saved_jobs(username)
        applied_jobs = applications_.get_applied_jobs(username)

        is_saved = any(job['Job Title'] == job_title for job in saved_jobs)
        is_applied = any(job['Job Title'] == job_title for job in applied_jobs)


        # Options
        print("Options:")

        if is_saved: print("  [1] Unsave this Job")
        else: print("  [1] Save this Job")

        if is_applied: print("  ")
        else: print("  [2] Apply for this Job")

        print("  [<] Return")
        print("")

        job_details_choice = input("Enter an option (or press Enter to access links): ")
        print("")


        if job_details_choice == "": home_.linkster()

        elif job_details_choice == "1":
            if is_saved:
                applications_.unsave_job(username, job_id)
            else:
                applications_.save_job(username, job_id)

        elif job_details_choice == "2" and not is_applied:
            applications_.apply_for_job(username, job_id)

        elif job_details_choice == "<": return

        else: print("Invalid choice. Please enter an available option.")


    else:
        print("Job details not found.")



                               #----------------#
#------------------------------#    Find Job    #------------------------------#
                               #----------------#

def find_job():

    # List all job titles
    job_titles = [job["Job Title"] for job in config.Jobs]


    while True:

        print("")
        print("Jobs Available:")
        for index, job_title in enumerate(job_titles, start=1):
            print(f"  [{index}] {job_title}")

        print("  [<] Return")
        print("")

        job_choice = input("Enter an option (or press Enter to access links): ")
        print("")

        if job_choice == "": home_.linkster()
        elif job_choice == "<": return

        elif job_choice.isdigit():

            selected_index = int(job_choice) - 1

            if 0 <= selected_index < len(job_titles):

                selected_job_title = job_titles[selected_index]

                for job in config.Jobs:

                    if job["Job Title"] == selected_job_title:
                        selected_job_id = job["Id"]

                display_job_details(selected_job_title, selected_job_id)

            else: print("Invalid choice. Please enter an available option.")

        else: print("Invalid choice. Please enter an available option.")




# End of File
