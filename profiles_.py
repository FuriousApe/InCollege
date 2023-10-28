
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

import accounts_
import config
import home_

from config import DBProfiles
from data_ import connect_to

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Load Profiles                              #
#                             [ 2 ] Save Profiles                              #
#                             [ 3 ] Print Section                              #
#                             [ 4 ] Display Profile                            #
#                                                                              #
#                             [ 5 ] Edit Profile                               #
#                             [ 6 ] Edit Bio                                   #
#                             [ 7 ] Edit Eduction                              #
#                             [ 8 ] Edit Job                                   #
#                                                                              #
#                             [ 9 ] Save Profile                               #
#                             [ 10 ] Get Profile                               #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

            # All functions that deal with profile creation are here. #

                             #---------------------#
#----------------------------#    Load Profiles    #---------------------------#
                             #---------------------#

            # Gets all profiles from profile database, returns them #

def load_profiles():

# Connect to Database

    connection, cursor = connect_to(DBProfiles)

    if connection is None:
        return

# Define Target Info

    query = '''
        SELECT
            username,
            title,
            about,

            job_1_title,
            job_1_employer,
            job_1_date_started,
            job_1_date_ended,
            job_1_location,
            job_1_description,

            job_2_title,
            job_2_employer,
            job_2_date_started,
            job_2_date_ended,
            job_2_location,
            job_2_description,

            job_3_title,
            job_3_employer,
            job_3_date_started,
            job_3_date_ended,
            job_3_location,
            job_3_description,

            college_name,
            college_major,
            college_years_attended
        FROM
             profiles;
        '''

# Execute Query

    try:
        cursor.execute(query)
        profiles_data = cursor.fetchall()
        config.Profiles = [{
            "Username": username,
            "Title": title,
            "About Me": about,

            "Job 1 : Title": job_1_title,
            "Job 1 : Employer": job_1_employer,
            "Job 1 : Date Started": job_1_date_started,
            "Job 1 : Date Ended": job_1_date_ended,
            "Job 1 : Location": job_1_location,
            "Job 1 : Description": job_1_description,

            "Job 2 : Title": job_2_title,
            "Job 2 : Employer": job_2_employer,
            "Job 2 : Date Started": job_2_date_started,
            "Job 2 : Date Ended": job_2_date_ended,
            "Job 2 : Location": job_2_location,
            "Job 2 : Description": job_2_description,

            "Job 3 : Title": job_3_title,
            "Job 3 : Employer": job_3_employer,
            "Job 3 : Date Started": job_3_date_started,
            "Job 3 : Date Ended": job_3_date_ended,
            "Job 3 : Location": job_3_location,
            "Job 3 : Description": job_3_description,

            "University": college_name,
            "Major": college_major,
            "Years Attended": college_years_attended
            } for (
                    username,
                    title,
                    about,
                    job_1_title,
                    job_1_employer,
                    job_1_date_started,
                    job_1_date_ended,
                    job_1_location,
                    job_1_description,
                    job_2_title,
                    job_2_employer,
                    job_2_date_started,
                    job_2_date_ended,
                    job_2_location,
                    job_2_description,
                    job_3_title,
                    job_3_employer,
                    job_3_date_started,
                    job_3_date_ended,
                    job_3_location,
                    job_3_description,
                    college_name,
                    college_major,
                    college_years_attended
                    ) in profiles_data]

    except sqlite3.Error as err:
        print("There was an error delivering the query: ", err)


# Close Connection

    finally:

        if connection:
            connection.commit()
            connection.close()

            return config.Profiles


                             #---------------------#
#----------------------------#    Save Profiles    #---------------------------#
                             #---------------------#

                  # Saves passed profiles to profile database #
                       # Called during create_profile() #

def save_profiles(profiles):

# Connect to Database

    connection, cursor = connect_to(DBProfiles)

    if connection is None:
        return

# Into These Columns...

    query = '''
        INSERT INTO profiles (
            username,
            title,
            about,

            job_1_title,
            job_1_employer,
            job_1_date_started,
            job_1_date_ended,
            job_1_location,
            job_1_description,

            job_2_title,
            job_2_employer,
            job_2_date_started,
            job_2_date_ended,
            job_2_location,
            job_2_description,

            job_3_title,
            job_3_employer,
            job_3_date_started,
            job_3_date_ended,
            job_3_location,
            job_3_description,

            college_name,
            college_major,
            college_years_attended
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''

# ...Insert This Data

    try:
        cursor.execute("DELETE FROM profiles;")

        for profile in profiles:
            cursor.execute(query,
                         (
                             profile['Username'],
                             profile['Title'],
                             profile['About Me'],

                             profile['Job 1 : Title'],
                             profile['Job 1 : Employer'],
                             profile['Job 1 : Date Started'],
                             profile['Job 1 : Date Ended'],
                             profile['Job 1 : Location'],
                             profile['Job 1 : Description'],

                             profile['Job 2 : Title'],
                             profile['Job 2 : Employer'],
                             profile['Job 2 : Date Started'],
                             profile['Job 2 : Date Ended'],
                             profile['Job 2 : Location'],
                             profile['Job 2 : Description'],

                             profile['Job 3 : Title'],
                             profile['Job 3 : Employer'],
                             profile['Job 3 : Date Started'],
                             profile['Job 3 : Date Ended'],
                             profile['Job 3 : Location'],
                             profile['Job 3 : Description'],

                             profile['University'],
                             profile['Major'],
                             profile['Years Attended']
                         )
                    )


# Error Handling

    except sqlite3.Error as err:
        print("There was an error delivering the query: ", err)


# Close Connection

    finally:

        if connection:
            connection.commit()
            connection.close()


                            #---------------------#
#---------------------------#    Print Section    #----------------------------#
                            #---------------------#

def print_section_info(title, info) :

    if info:
        print(f"  {title} : {textwrap.fill(info, width=25)}\n")
        #print("  " + "-" * len(title))
        #print(f"  {textwrap.fill(info, width=25)}\n")
    else:
        print(f"  {title} : No info\n")


                           #-----------------------#
#--------------------------#    Display Profile    #---------------------------#
                           #-----------------------#

def display_profile(username) :

    while True:


# Check if the profile is the user's or a friend's

        if username == config.User['Username']:
            user_profile = True
            profile = config.UserProfile
            account = config.User
        else:
            user_profile = False
            profile = get_profile(username)
            account = accounts_.get_account(username)


# Store information to be displayed

        f_name = account['First Name']
        l_name = account['Last Name']

        title = profile.get('Title', '')
        about = profile.get('About Me', '')

        college_name = account.get('University', '')
        config.UserProfile['University'] = college_name
        college_major = account.get('Major', '')
        config.UserProfile['Major'] = college_major

        college_years_attended = profile.get('Years Attended', '')




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
        print_section_info("University", college_name)
        print_section_info("Major", college_major)
        print_section_info("Years Attended", college_years_attended)



# Create 'job' array, use it to check for content presence
# This is where the job info is collected

        job = []

        for i in range(1,4):

            # '.get()' returns the 2nd argument if the 1st doesn't exist
            job_info = {
                f'Job {i} : Title': profile.get(f'Job {i} : Title', ''),
                f'Job {i} : Employer' : profile.get(f'Job {i} : Employer', ''),
                f'Job {i} : Date Started': profile.get(f'Job {i} : Date Started', ''),
                f'Job {i} : Date Ended': profile.get(f'Job {i} : Date Ended', ''),
                f'Job {i} : Location': profile.get(f'Job {i} : Location', ''),
                f'Job {i} : Description': profile.get(f'Job {i} : Description', '')
            }

# If no content for any of the 3 jobs, don't display that job section
# This is where the job info is displayed


            if any(job_info.values()):
                print(f"\n|::::::::::::::::::::::::::::|")
                print(f"|         Job {i} Info         |")
                print(f"|::::::::::::::::::::::::::::|\n")

                for field, value in job_info.items():
                    if value:
                        print_section_info(field, value)

#            for content in range(0,6):
#                if job[content]:
#
#                    print("")
#                    print("|::::::::::::::::::::::::::::|")
#                    print("")
#                    print_section_info(f"Job {i} Title", job[0])
#                    print_section_info(f"Job {i} Employer", job[1])
#                    print_section_info(f"Job {i} Date Started", job[2])
#                    print_section_info(f"Job {i} Date Ended", job[3])
#                    print_section_info(f"Job {i} Location", job[4])
#                    print_section_info(f"Job {i} Description", job[5])
#                    break


# If it's the user's profile (not a friend's), allow editing option

        if user_profile: print("  [1] Edit Profile")
        print("  [<] Return")


# Take input

        while True:

            profile_choice = input("Enter an option (or press Enter to access links): ")

            if profile_choice == '': home_.linkster(); break
            elif profile_choice == '<': return
            elif user_profile and profile_choice == '1': edit_profile(); break
            else: print("Invalid input. Please enter one of the available options.")



                             #--------------------#
#----------------------------#    Edit Profile    #----------------------------#
                             #--------------------#

def edit_profile() :


# If it's the user's first time, make note of it in User[]

    if config.User['Created a Profile']:
        print("")
        print(":::::::::  Welcome back!  :::::::::")
        print("")

    else :
        config.User['Created a Profile'] = True

        # Save change
        accounts = accounts_.load_accounts()
        for account in accounts:
            if account["Username"] == config.User["Username"]:
                account['Created a Profile'] = True
        accounts_.save_accounts(accounts)

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

        edit_choice = input("Enter an option (or press Enter to access links): ")


# Allow user to edit profile, display profile, go back, or access linkster()

        if edit_choice == '': home_.linkster()
        elif edit_choice == '<': return
        elif edit_choice == '>': display_profile(config.User['Username'])
        elif edit_choice == 'i': edit_bio()
        elif edit_choice == 'e': edit_ed()
        elif (edit_choice == '1' or
              edit_choice == '2' or
              edit_choice == '3' ): edit_job(edit_choice)

        else: print("Invalid input. Please enter one of the available options.")


                               #----------------#
#------------------------------#    Edit Bio    #------------------------------#
                               #----------------#

def edit_bio() :

    while True:

        title = textwrap.fill(config.UserProfile.get('Title', ''), width=25)
        about_me = textwrap.fill(config.UserProfile.get('About Me', ''), width=25)

        print("")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("  Which section would you like to edit?  ")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("")

        print(f"  [1] Title: {title}")
        print(f"  [2] About Me: {about_me}")

        print("  [<] Return")

        bio_choice = input("Enter an option (or press Enter to access links): ")

        if bio_choice == '': home_.linkster()
        elif bio_choice == '<': return
        elif bio_choice == '1': config.UserProfile['Title'] = input("Title:")
        elif bio_choice == '2': config.UserProfile['About Me'] = input("About Me:")

        else: print("Invalid input. Please enter one of the available options.")
        save_profile(config.UserProfile)



                               #---------------#
#------------------------------#    Edit Ed    #-------------------------------#
                               #---------------#

def edit_ed() :

    while True:

        university = textwrap.fill(config.UserProfile.get('University', ''), width=25)
        major = textwrap.fill(config.UserProfile.get('Major', ''), width=25)
        years_attended = textwrap.fill(config.UserProfile.get('Years Attended', ''), width=25)

        print("")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("  Which section would you like to edit?  ")
        print("|:::::::::::::::::::::::::::::::::::::::|")
        print("")

        print(f"  [1] University: {university}")
        print(f"  [2] Major: {major}")
        print(f"  [3] Years Attended: {years_attended}")

        print("  [<] Return")

        ed_choice = input("Enter an option (or press Enter to access links): ")

        if ed_choice == '': home_.linkster()
        elif ed_choice == '<': return
        elif ed_choice == '1':
            university = input("University:")
            university = university.title()
            config.User['University'] = university
            config.UserProfile['University'] = university
        elif ed_choice == '2':
            major = input("Major:")
            major = major.title()
            config.User['Major'] = major
            config.UserProfile['Major'] = major
        elif ed_choice == '3':
            years_attended = input("Years Attended:")
            config.UserProfile['Years Attended'] = years_attended

        else: print("Invalid input. Please enter one of the available options.")

        for account in config.Accounts:
            if account['Username'] == config.User['Username']:
                account['University'] = config.User['University']
                account['Major'] = config.User['Major']

        accounts_.save_accounts(config.Accounts)
        save_profile(config.UserProfile)



                               #----------------#
#------------------------------#    Edit Job    #------------------------------#
                               #----------------#

def edit_job(job_number) :

    while True:

        title = textwrap.fill(config.UserProfile.get(f'Job {job_number} : Title', ''), width=25)
        employer = textwrap.fill(config.UserProfile.get(f'Job {job_number} : Employer', ''), width=25)
        date_started = textwrap.fill(config.UserProfile.get(f'Job {job_number} : Date Started', ''), width=25)
        date_ended = textwrap.fill(config.UserProfile.get(f'Job {job_number} : Date Ended', ''), width=25)
        location = textwrap.fill(config.UserProfile.get(f'Job {job_number} : Location', ''), width=25)
        description = textwrap.fill(config.UserProfile.get(f'Job {job_number} : Description', ''), width=25)

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

        job_choice = input("Enter an option (or press Enter to access links): ")

        if job_choice == '': home_.linkster()
        elif job_choice == '<': return
        elif job_choice == '1': config.UserProfile[f'Job {job_number} : Title'] = input("Title:")
        elif job_choice == '2': config.UserProfile[f'Job {job_number} : Employer'] = input("Employer:")
        elif job_choice == '3': config.UserProfile[f'Job {job_number} : Date Started'] = input("Date Started:")
        elif job_choice == '4': config.UserProfile[f'Job {job_number} : Date Ended'] = input("Date Ended:")
        elif job_choice == '5': config.UserProfile[f'Job {job_number} : Location'] = input("Location:")
        elif job_choice == '6': config.UserProfile[f'Job {job_number} : Description'] = input("Description:")

        else: print("Invalid input. Please enter one of the available options.")
        save_profile(config.UserProfile)




                             #--------------------#
#----------------------------#    Save Profile    #----------------------------#
                             #--------------------#

              # Saves the given profile to the 'profiles' database #

def save_profile(profile) :

    all_profiles = load_profiles()

    for a in all_profiles:
        if a['Username'].strip().lower() == profile["Username"].strip().lower():
            all_profiles.remove(a)
            all_profiles.append(profile)

#    for a in all_profiles:
#        if 'Username' in a and a['Username'].strip().lower() == profile['Username'].strip().lower():
#            for key, value in profile.items():
#                a[key] = value

    save_profiles(all_profiles)




                             #-------------------#
#----------------------------#    Get Profile    #-----------------------------#
                             #-------------------#

            # Finds the profile with the given username and returns it #

def get_profile(username) :

    # Prepare for Comparison

    username = username.strip().lower()
    profiles = load_profiles()


    # Search Profiles

    for profile in profiles:

        profile_username = profile["Username"].strip().lower()
        if profile_username == username: return profile

    return None
