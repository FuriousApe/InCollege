
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

import applications_
import home_
from data_ import connect_to_database

from classes.JobPost import JobPost

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Parse Salary                               #
#                             [ 2 ] Count Jobs                                 #
#                             [ 3 ] Post Job                                   #
#                                                                              #
#                             [ 4 ] Job Menu                                   #
#                             [ 5 ] Applied Jobs Menu                          #
#                             [ 6 ] Saved Jobs Menu                            #
#                             [ 7 ] Display Job Details                        #
#                             [ 8 ] Find Job Menu                              #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                             #--------------------#
#----------------------------#    Parse Salary    #----------------------------#
                             #--------------------#

           # Removes any unwanted characters that may have been input #

def parse_salary():

    while True:

        # Prompt
        salary = input("  Salary: ")

        # Replace Unwanted Characters
        salary = salary.replace('$', '')
        salary = salary.replace(',', '')

        if salary.replace('.', '').isdigit(): break

        # Error Handling
        else: print("Invalid salary - please input only numeric values.")

    return float(salary)


                              #------------------#
#-----------------------------#    Count Jobs    #-----------------------------#
                              #------------------#

  # Counts number of jobs in database, returns True if there's room for more #

def room_for_job():

    jobs = JobPost.fetch_all()

    if jobs:
        job_count = len(jobs)
        return job_count < config.MaxJobs

    else: return True


                               #----------------#
#------------------------------#    Post Job    #------------------------------#
                               #----------------#

         # Gets information about job from user, saves it to database #

def post_job_menu():

    username = config.user.username

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
        job = JobPost(
            job_title = job_title,
            description = description,
            location = location,
            employer = employer,
            salary = salary,
            username = username
        )

        # Save to DB
        job.post()
        print("Your job has been posted!")

    # If Database is Full
    else:
        print("")
        print("We're sorry. Our 'Jobs' database is currently full.")
        print("Please return later when there is room for another posting.")
        print("")
        print("Have a nice day.")


#------------------------------#----------------#------------------------------#
#------------------------------#    Job Menu    #------------------------------#
#------------------------------#----------------#------------------------------#

       # Provides option to find a job, find an internship, or post a job #
                      # One of the paths from home() #

def job_menu():

    user = config.user

    # Fetch notifications for the user
    notifications = user.fetch_notifications()

    # If there are any, display and delete them
    for message in notifications:
        print(f"\n*-*-*\nNotification: {message}\n*-*-*\n")

    # Deleting them
    if notifications: user.delete_notifications()

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
        print("      [5] Applied Jobs")
        print("       [6] Return")
        print("")

        choice = input("Enter an option (or press Enter to access links): ")
        print("")

        # Outcomes
        if choice == "": home_.linkster()
        elif choice == "1": find_job_menu()
        elif choice == "2": config.under_construction()
        elif choice == "3": post_job_menu()
        elif choice == "4": saved_jobs_menu()
        elif choice == "5": applied_jobs_menu()

        elif choice == "6": return
        else: print("Invalid choice. Please enter an available option.")




#---------------------------#-------------------------#--------------------------#
#---------------------------#    Applied Jobs Menu    #--------------------------#
#---------------------------#-------------------------#--------------------------#

def applied_jobs_menu():

    while True:

        print("")
        print("|---------------------------|")
        print("        Applied Jobs         ")
        print("|---------------------------|")
        print("")

        applied_jobs = JobPost.get_applied_jobs(config.user.username)

        if not applied_jobs:
            print("No applied jobs found.")
            return

        # Get applied job titles and IDs
        titles = [job.job_title for job in applied_jobs]
        ids = [job.job_id for job in applied_jobs]

        # Display titles
        for index, title in enumerate(titles, start=1):
            print(f"  [{index}] {title}")

        print("  [<] Return")
        print("")

        choice = input("Enter an option (or press Enter to access links): ")
        print("")

        if choice == "": home_.linkster()
        elif choice == "<": return
        elif choice.isdigit():
            chosen_index = int(choice) - 1
            if 0 <= chosen_index < len(titles):
                chosen_title = titles[chosen_index]
                chosen_id = ids[chosen_index]
                display_job_details(chosen_title, chosen_id)
            else:
                print("Invalid choice. Please select an available option.")

        else: print("Invalid choice. Please select an available option.")



# ---------------------------#-----------------------#--------------------------#
# ---------------------------#    Saved Jobs Menu    #--------------------------#
# ---------------------------#-----------------------#--------------------------#

def saved_jobs_menu():

    while True:

        print("")
        print("|-------------------------|")
        print("        Saved Jobs         ")
        print("|-------------------------|")
        print("")

        saved_jobs = JobPost.get_saved_jobs(config.user.username)

        if not saved_jobs:
            print("No saved jobs found.")
            return

        # Get saved job titles and IDs
        titles = [job.job_title for job in saved_jobs]
        ids = [job.job_id for job in saved_jobs]

        # Display titles
        for index, title in enumerate(titles, start=1):
            print(f"  [{index}] {title}")

        print("  [<] Return")
        print("")

        choice = input("Enter an option (or press Enter to access links): ")
        print("")

        if choice == "": home_.linkster()
        elif choice == "<": return
        elif choice.isdigit():
            chosen_index = int(choice) - 1
            if 0 <= chosen_index < len(titles):
                chosen_title = titles[chosen_index]
                chosen_id = ids[chosen_index]
                display_job_details(chosen_id)
            else:
                print("Invalid choice. Please select an available option.")

        else:
            print("Invalid choice. Please select an available option.")




                          #---------------------------#
#-------------------------#    Display Job Details    #------------------------#
                          #---------------------------#

def display_job_details(job_id):

    username = config.user.username
    job = JobPost.fetch(job_id)

    if not job:
        print("Job details not found.")
        return

    print(f"Job Title: {job.job_title}")
    print(f"Description: {job.description}")
    print(f"Location: {job.location}")
    print(f"Employer: {job.employer}")
    print(f"Salary: ${job.salary:.2f}")
    print("")

    saved = job.is_saved_by(username)
    applied = job.has_applied(username)
    user_poster = job.username == username

    # Define available options
    options = {
        "1": ("Unsave this Job" if saved else "Save this Job", lambda: job.unsave(username) if saved else job.save(username)),
        "2": ("Apply for this Job", lambda: applications_.apply_for_job(username, job)) if not applied else None,
        "3": ("Delete this Job", lambda: (job.delete(username), print("Job deleted successfully."))) if user_poster else None,
        "<": ("Return", lambda: None)
    }

    # Display options
    print("Options:")
    for key, value in options.items():
        if value:
            text, _ = value
            print(f"  [{key}] {text}")
    print("")

    # Get user choice and execute corresponding action
    choice = input("Enter an option (or press Enter to access links): ")
    print("")

    if choice == "":
        home_.linkster()
    elif choice in options and options[choice]:
        _, action = options[choice]
        action()
    else:
        print("Invalid choice. Please enter an available option.")



                               #----------------#
#------------------------------#    Find Job    #------------------------------#
                               #----------------#

def find_job_menu():

    # Dictionary: {job_title: JobPost Object}
    jobs = {job.job_title: job for job in JobPost.fetch_all()}

    while True:

        print("\nJobs Available:")
        for index, title in enumerate(jobs.keys(), start=1):
            print(f"  [{index}] {title}")

        print("  [<] Return\n")

        choice = input("Enter an option (or press Enter to access links): ")
        print("")

        if choice == "": home_.linkster()
        elif choice == "<": return

        elif choice.isdigit():
            chosen_index = int(choice) - 1
            titles_list = list(jobs.keys())

            if 0 <= chosen_index < len(titles_list):
                chosen_title = titles_list[chosen_index]
                chosen_id = jobs[chosen_title].job_id
                display_job_details(chosen_id)

            else:
                print("Invalid choice. Please enter an available option.")
        else:
            print("Invalid choice. Please enter an available option.")




# End of File
