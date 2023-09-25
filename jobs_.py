
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

from data_ import jobs_connect



                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Parse Salary                               #
#                             [ 2 ] Count Jobs                                 #
#                             [ 3 ] Post Job                                   #
#                             [ 4 ] Save Job                                   #
#                             [ 5 ] Job Menu                                   #
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
        salary = input("  Salary: ")

        salary = salary.replace('$', '')
        salary = salary.replace(',', '')

        if salary.replace('.', '').isdigit(): break

        else:
            print("Invalid salary - please input only numeric values.")

    return float(salary)

                                  # ---------------------#
    # ----------------------------#      Load Jobs       #---------------------------#
                                  # ---------------------#

    # Gets all jobs from job posting database, returns them. #
    # Called in count jobs

def load_jobs():

    # Connect to Database

    connection, cursor = jobs_connect()

    if connection is None:
        return

    # Define Target Info

    query = '''
        SELECT
            id,
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
        jobs = [{
            "Id": id,
            "Job Title": job_title,
            "Description": description,
            "Location": location,
            "Employer": employer,
            "Salary": salary,
            "First Name": first_name,
            "Last Name": last_name
        } for id, job_title, description, location, employer, salary, first_name, last_name in jobs_data]

    except sqlite3.Error as err:
        print("There was an error delivering the query: ", err)


    # Close Connection

    finally:

        if connection:
            connection.commit()
            connection.close()

            return jobs


                              #------------------#
#-----------------------------#    Count Jobs    #-----------------------------#
                              #------------------#

  # Counts number of jobs in database, returns True if there's room for more #
                     # Called at beginning of post_job() #

def room_for_job():
    jobs = load_jobs()
    job_count = len(jobs);

    return job_count < config.MaxJobs





                               #----------------#
#------------------------------#    Post Job    #------------------------------#
                               #----------------#

         # Gets information about job from user, saves it to database #
                       # One of the options in job_menu() #

def post_job(first_name, last_name):


    print("")
    print("|------------|")
    print("  Post a Job  ")
    print("|------------|")
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

        save_job(job)
        print("Your job has been posted!")


# If Database is Full

    else:
        print("")
        print("We're sorry. Our 'Jobs' database is currently full.")
        print("Please return later when there is room for another posting.")
        print("")
        print("Have a nice day.")



                               #----------------#
#------------------------------#    Save Job    #------------------------------#
                               #----------------#

          # Takes a dict of job info, uploads it to the job database #
                   # Called during the post_job() function #

def save_job(job):


# Connect to DB

    connection, cursor = jobs_connect()


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




#------------------------------#----------------#------------------------------#
#------------------------------#    Job Menu    #------------------------------#
#------------------------------#----------------#------------------------------#

       # Provides option to find a job, find an internship, or post a job #
                      # One of the paths from home() #

def job_menu():


    print("")
    print("|-------------------------|")
    print("  Job Search / Internship  ")
    print("|-------------------------|")
    print("")


# Options

    print("  [1] Find a Job")
    print("   [2] Find an Internship")
    print("    [3] Post a Job")
    print("     [4] Return")
    print("")

    jobs_choice = input("Enter an option (1-4): ")
    print("")


# Outcomes

    if jobs_choice == "1":

        print("")
        print("  / / / / / / / / / / / / / / / / / / / /")
        print(" / / / / /  UNDER CONSTRUCTION / / / / /")
        print("/ / / / / / / / / / / / / / / / / / / /")
        print("")


    elif jobs_choice == "2":

        print("")
        print("  / / / / / / / / / / / / / / / / / / / /")
        print(" / / / / /  UNDER CONSTRUCTION / / / / /")
        print("/ / / / / / / / / / / / / / / / / / / /")
        print("")


    elif jobs_choice == "3":
        post_job(
            config.User["First Name"],
            config.User["Last Name"]
            )

    elif jobs_choice == "4":
        return

    else:
        print("Invalid choice. Please select a number 1-4.")



# End of File
