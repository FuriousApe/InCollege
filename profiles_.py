
                          #############################
###############################                   ##############################
###############################  P R O F I L E S  ##############################
###############################                   ##############################
                          #############################

                  # All code pertaining to the user's profile. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3
import textwrap

import config
import home_
from classes.User import User
from classes.UserProfile import UserProfile


                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Print Section                              #
#                             [ 2 ] Display Profile                            #
#                                                                              #
#                             [ 3 ] Edit Profile                               #
#                             [ 4 ] Edit Bio                                   #
#                             [ 5 ] Edit Eduction                              #
#                             [ 6 ] Edit Job                                   #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

              # All menus that deal with profile creation are here. #

                            #---------------------#
#---------------------------#    Print Section    #----------------------------#
                            #---------------------#

def print_section_info(title, info) :

    if info:
        print(f"  {title} : {textwrap.fill(info, width=25)}\n")
    else:
        print(f"  {title} : No info\n")


                           #-----------------------#
#--------------------------#    Display Profile    #---------------------------#
                           #-----------------------#

def display_profile(username):

    while True:

        # Check if the profile is the user's or a friend's
        if username == config.user.username:
            user_profile = True
            profile = config.profile
            user = config.user
        else:
            user_profile = False
            profile = UserProfile.fetch(username)
            user = User.fetch(username)

        # Store information to be displayed
        f_name = user.first_name
        l_name = user.last_name

        title = profile.title
        about = profile.about
        university = profile.university
        major = profile.major
        years_attended = profile.years_attended

        print("")
        print("|=============================")
        print(f"  {f_name} {l_name}")
        print("|-----------------------------")
        print("")
        print_section_info("Title", title)
        print("")
        print("|::::::::::::::::::::::::::::|")
        print("")
        print_section_info("About Me", about)

        print("")
        print("|::::::::::::::::::::::::::::|")
        print("")
        print_section_info("University", university)
        print_section_info("Major", major)
        print_section_info("Years Attended", years_attended)

        # Create 'job' array, use it to check for content presence
        for i in range(1, 4):

            job_info = {
                f'Job {i} : Title': getattr(profile, f'job_{i}_title', ''),
                f'Job {i} : Employer': getattr(profile, f'job_{i}_employer', ''),
                f'Job {i} : Date Started': getattr(profile, f'job_{i}_date_started', ''),
                f'Job {i} : Date Ended': getattr(profile, f'job_{i}_date_ended', ''),
                f'Job {i} : Location': getattr(profile, f'job_{i}_location', ''),
                f'Job {i} : Description': getattr(profile, f'job_{i}_description', '')
            }

            # If no content for any of the 3 jobs, don't display that job section
            if any(job_info.values()):
                print(f"\n|::::::::::::::::::::::::::::::|")
                print(f"|         Job {i} Info         |")
                print(f"|::::::::::::::::::::::::::::::|\n")

                for field, content in job_info.items():
                    if content: print_section_info(field, content)

        # If it's the user's profile (not a friend's), allow editing
        if user_profile: print("  [1] Edit Profile")
        print("  [<] Return")

        # Take input
        while True:

            choice = input("Enter an option (or press Enter to access links): ")

            if choice == '':
                home_.linkster()
                break
            elif choice == '<':
                return
            elif user_profile and choice == '1':
                menu()
                break
            else:
                print("Invalid input. Please enter one of the available options.")



                             #--------------------#
#----------------------------#    Edit Profile    #----------------------------#
                             #--------------------#

def menu() :

    user = config.user

    # If it's the user's first time, make note of it in User[]
    if user.created_a_profile:
        print("")
        print(":::::::::  Welcome back!  :::::::::")
        print("")

    else :
        user.created_a_profile = True
        user.save()

        print("")
        print("::::::::::  Profile Created  ::::::::::::")
        print("")

    # Proceed with Profile editing
    while True:

        print("")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("  Which section would you like to edit?  ")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("")

        print("  [i] Bio")
        print("  [e] Education")
        print("  [1] Job 1")
        print("  [2] Job 2")
        print("  [3] Job 3")

        print("")
        print("  [<] Return        Display Profile [>]  ")

        choice = input("Enter an option (or press Enter to access links): ")

        # Allow user to edit profile, display profile, go back, or access linkster()
        if choice == '': home_.linkster()
        elif choice == '<': return
        elif choice == '>': display_profile(user.username)
        elif choice == 'i': edit_bio()
        elif choice == 'e': edit_ed()
        elif (choice == '1' or
              choice == '2' or
              choice == '3' ): edit_job(choice)

        else: print("Invalid input. Please enter one of the available options.")


                               #----------------#
#------------------------------#    Edit Bio    #------------------------------#
                               #----------------#

def edit_bio() :

    while True:

        profile = config.profile

        title = textwrap.fill(profile.title, width=25)
        about_me = textwrap.fill(profile.about, width=25)

        print("")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("  Which section would you like to edit?  ")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("")

        print(f"  [1] Title: {title}")
        print(f"  [2] About Me: {about_me}")

        print("  [<] Return")

        choice = input("Enter an option (or press Enter to access links): ")

        if choice == '': home_.linkster()
        elif choice == '<': return
        elif choice == '1': profile.title = input("Title:")
        elif choice == '2': profile.about = input("About Me:")

        else: print("Invalid input. Please enter one of the available options.")

        profile.save()



                               #---------------#
#------------------------------#    Edit Ed    #-------------------------------#
                               #---------------#

def edit_ed() :

    while True:

        user = config.user
        profile = config.profile

        university = textwrap.fill(profile.university, width=25)
        major = textwrap.fill(profile.major, width=25)
        years_attended = textwrap.fill(profile.years_attended, width=25)

        print("")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("  Which section would you like to edit?  ")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("")

        print(f"  [1] University: {university}")
        print(f"  [2] Major: {major}")
        print(f"  [3] Years Attended: {years_attended}")

        print("  [<] Return")

        choice = input("Enter an option (or press Enter to access links): ")

        if choice == '': home_.linkster()
        elif choice == '<': return

        elif choice == '1':
            university = input("University:")
            university = university.title()
            user.university = university
            profile.university = university

        elif choice == '2':
            major = input("Major:")
            major = major.title()
            user.major = major
            profile.major = major

        elif choice == '3':
            years_attended = input("Years Attended:")
            profile.years_attended = years_attended

        else: print("Invalid input. Please enter one of the available options.")

        user.save()
        profile.save()



                               #----------------#
#------------------------------#    Edit Job    #------------------------------#
                               #----------------#

def edit_job(job_number):

    job_number = int(job_number)

    while True:

        profile = config.profile
        job = profile.jobs[job_number-1]

        title = textwrap.fill(job.title, width=25)
        employer = textwrap.fill(job.employer, width=25)
        date_started = textwrap.fill(job.date_started, width=25)
        date_ended = textwrap.fill(job.date_ended, width=25)
        location = textwrap.fill(job.location, width=25)
        description = textwrap.fill(job.description, width=25)

        print("")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("  Which section would you like to edit?  ")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("")

        print(f"  Job {job_number}")
        print("")
        print(f"  [1] Title: {title}")
        print(f"  [2] Employer: {employer}")
        print(f"  [3] Date Started: {date_started}")
        print(f"  [4] Date Ended: {date_ended}")
        print(f"  [5] Location: {location}")
        print(f"  [6] Description: {description}")

        print("  [<] Return")

        choice = input("Enter an option (or press Enter to access links): ")

        if choice == '': home_.linkster()
        elif choice == '<': return

        elif choice == '1': job.title = input("Title:")
        elif choice == '2': job.employer = input("Employer:")
        elif choice == '3': job.date_started = input("Date Started:")
        elif choice == '4': job.date_ended = input("Date Ended:")
        elif choice == '5': job.location = input("Location:")
        elif choice == '6': job.description = input("Description:")

        else: print("Invalid input. Please enter one of the available options.")

        profile.save()





# End of file
