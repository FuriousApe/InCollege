
                          #############################
###############################                   ##############################
###############################  A C C O U N T S  ##############################
###############################                   ##############################
                          #############################

                       # All code pertaining to accounts. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3

import config
import home_
import settings_
import profiles_

from config import DBAccounts
from data_ import connect_to

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Load Accounts                              #
#                             [ 2 ] Save Accounts                              #
#                             [ 3 ] Find Account                               #
#                                                                              #
#                             [ 4 ] Create Username                            #
#                             [ 5 ] Create Password                            #
#                             [ 6 ] Check Number of Accounts                   #
#                             [ 7 ] Validate Credentials                       #
#                             [ 8 ] Create Account                             #
#                                                                              #
#                             [ 9 ] Get Profile Info                           #
#                             [ 10 ] Log In                                    #
#                             [ 11 ] Log Out                                   #
#                             [ 12 ] Login Menu                                #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

             # All functions that deal with account info are here. #

                             #---------------------#
#----------------------------#    Load Accounts    #---------------------------#
                             #---------------------#

            # Gets all accounts from student database, returns them. #
                 # Called during create_account() and login() #

def load_accounts():


# Connect to Database

    connection, cursor = connect_to(DBAccounts)

    if connection is None:
        return


# Define Target Info

    query = '''
        SELECT
            username,
            password,
            first_name,
            last_name,
            university,
            major
        FROM
            accounts;
    '''


# Execute Query

    try:
        cursor.execute(query)
        accounts_data = cursor.fetchall()
        config.Accounts = [{
                    "Username": username,
                    "Password": password,
                    "First Name": first_name,
                    "Last Name": last_name,
                    "University": university,
                    "Major": major
                    } for username, password, first_name, last_name, university, major in accounts_data]

    except sqlite3.Error as err:
        print("There was an error delivering the query: ", err)


# Close Connection

    finally:

        if connection:
            connection.commit()
            connection.close()

            return config.Accounts



                             #---------------------#
#----------------------------#    Save Accounts    #---------------------------#
                             #---------------------#

                  # Saves passed accounts to student database #
                        # Called during create_account() #

def save_accounts(accounts):


# Connect to Database

    connection, cursor = connect_to(DBAccounts)

    if connection is None:
        return


# Into These Columns...

    query = '''
        INSERT INTO accounts (
            username,
            password,
            first_name,
            last_name,
            university,
            major
        )
        VALUES (?, ?, ?, ?, ?, ?);
    '''


# ...Insert This Data

    try:
        cursor.execute("DELETE FROM accounts;")

        for account in accounts:
            cursor.execute(query,
                (
                    account['Username'],
                    account['Password'],
                    account['First Name'],
                    account['Last Name'],
                    account['University'],
                    account['Major']
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



                              #--------------------#
#-----------------------------#    Find Account    #---------------------------#
                              #--------------------#

        # Searches accounts database for a first and last name argument #
                          # Returns the account or None #

def find_account(first_name, last_name):


# Prepare for Comparison

    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()

    accounts = load_accounts()


# Search Accounts

    for account in accounts:

        account_first_name = account["First Name"].strip().lower()
        account_last_name = account["Last Name"].strip().lower()

        if (
            account_first_name == first_name
            and
            account_last_name == last_name
            ):

            return account

        return None



                             #---------------------#
#----------------------------#   Create Username   #---------------------------#
                             #---------------------#

               # Checks passed username against passed accounts #
                        # Called during create_account() #

def create_username(username, accounts):


    if any(account["Username"] == username for account in accounts):
        return False

    else:
        return True


                             #---------------------#
#----------------------------#   Create Password   #---------------------------#
                             #---------------------#

                # Checks password argument against requirements #
                        # Called during create_account() #

def create_password(password):


    if (
        config.PasswordMinLength > len(password)
        or config.PasswordMaxLength < len(password)
        or not any(c.isupper() for c in password)
        or not any(c.isdigit() for c in password)
        or not any(c.isascii()
        and not c.isalnum() for c in password)
    ):
        return False


    else:
        return True


                        #------------------------------#
#-----------------------#   Check Number of Accounts   #-----------------------#
                        #------------------------------#

     # Checks the number of elements in passed data against global limit. #
                        # Called during create_account() #

def check_num_accounts(accounts):


    if len(accounts) >= config.MaxAccounts:
        print("All permitted accounts have been created, please come back later.")
        return False

    else:
        print("Good news! We've got room for you!")
        print("")
        return True



                         #----------------------------#
#------------------------#    Validate Credentials    #------------------------#
                         #----------------------------#

      # Checks the passed username/password with the passed account list #
                          # Called during login() #

def validate_credentials(username, password, accounts):


    for account in accounts:

        if (
            account["Username"] == username
            and
            account["Password"] == password
        ):

            return "You have successfully logged in."

    return "Incorrect username/password, please try again."



                            #----------------------#
#---------------------------#    Create Account    #---------------------------#
                            #----------------------#

          # Gets user info, checks requirements, saves them to database #
                    # One of the paths from login_menu() #

def create_account():


    accounts = load_accounts()
    result = check_num_accounts(accounts)

    if not result:
        return

    print("")
    print("|----------------------------|")
    print("       Account Creation       ")
    print("|----------------------------|")
    print("")


# Entering Personal Info

    while True:

        first_name = input("First Name: ")
        if not first_name:
            print("")
            print("You must enter your first name to continue.")
            print("")
            continue
        else:
            break

    while True:
        last_name = input("Last Name: ")
        if not last_name:
            print("")
            print("You must enter your last name to continue.")
            print("")
            continue
        else:
            break

    while True:
        university = input("University: ")

        if not university:
            print("")
            print("You must enter your university to continue.")
            print("")
            continue
        else:
            university = ' '.join([word.capitalize() for word in university.split()])
            break

    while True:
        major = input("Major: ")

        if not major:
            print("")
            print("You must enter your major to continue.")
            print("")
            continue
        else:
            major = ' '.join([word.capitalize() for word in major.split()])
            break


# Creating a Username

    while True:

        username = input("Enter a username: ")
        if not username:
            return "You must enter a username."

        valid = create_username(username, accounts)
        if valid:
            break

        else:
            print("This username already exists. Please choose a different one.")


# Creating a Password

    while True:
        password = input("Enter a password: ")
        valid = create_password(password)

        if not valid:
            print("-------------------------------")
            print("Invalid password. Requirements:")
            print("   [*] Character length: 8-12")
            print("   [*] Must contain at least 1 uppercase letter")
            print("   [*] Must contain at least 1 digit")
            print("   [*] Must contain at least 1 special character")
            continue

        else:
            break


# Saving to Database

    accounts.append({
                    "Username": username,
                    "Password": password,
                    "First Name": first_name,
                    "Last Name": last_name,
                    "University": university,
                    "Major": major
                    })
    save_accounts(accounts)
    settings_.initialize_user(username)

    print("")
    print("Account created successfully.")
    print("")


# Profile Creation

    while True:
        print("")
        creating_profile = input("Since you're here, would you like to create your profile? (Y/N):")
        print("")

        creating_profile.upper()

        if creating_profile == 'Y':
            profiles_.edit_profile()
            continue

        elif creating_profile == 'N':
            print("No problem! You can create your profile at any time from the Home Screen.")
            break

        else:
            print("Invalid input. Please enter either Y (for yes) or N (for no).")


                           #------------------------#
#--------------------------#    Get Account Info    #--------------------------#
                           #------------------------#

      # Returns the username, password, first name, and last name as dict #
                # Stores dict in global var 'User' during login() #

def get_account(username):

    try:
        config.Connection, cursor = connect_to(DBAccounts)

        if config.Connection is None:
            return


# Define fields

        query = '''
            SELECT
                username,
                password,
                first_name,
                last_name,
                university,
                major
            FROM
                accounts
            WHERE
                username = ?
        '''


# Execute query

        cursor.execute(query, (username,))
        user_data = cursor.fetchone()

        config.User = {
                    "Username": user_data[0],
                    "Password": user_data[1],
                    "First Name": user_data[2],
                    "Last Name": user_data[3],
                    "University": user_data[4],
                    "Major": user_data[5],
                    }


# Error Handling

    except sqlite3.Error as err:
        print("There was an error fetching your information from the database: ", err)


# Close and Return

    finally:
        if config.Connection:
            config.Connection.commit()
            config.Connection.close()

            return config.User


                                 #-------------#
#--------------------------------#    Login    #-------------------------------#
                                 #-------------#

   # Performs the login function, accepts or rejects the username/password #
                    # One of the paths from login_menu() #

def login():


# Get Credentials

    while True:

        username = input("Username: ")
        password = input("Password: ")


# Cross-check with Accounts

        accounts = load_accounts()
        result = validate_credentials(username, password, accounts)


# Outcomes

        if result == "You have successfully logged in.":

            print(result)
            config.User = get_account(username)     # Load account details into config.py

            settings_.load_user_settings()      # Do the same with their settings
            settings_.initialize_settings_database()
            home_.home()

            return

        else:
            print("")
            print("X------------X------------X------------X------------X")
            print("|   Incorrect username/password, please try again.  |")
            print("X------------X------------X------------X------------X")

            choice = input('''
                Press 'Enter' now to try again or
                any other key to return to the opening menu:
                ''')

            if choice:
                return


                                 #--------------#
#--------------------------------#    Logout    #------------------------------#
                                 #--------------#

            # Logs the user out; resets all global variables to default #
                          # One of the paths from home() #

def logout():

    config.User = None
    config.UserSettings = None



#------------------------------#------------------#----------------------------#
#------------------------------#    Login Menu    #----------------------------#
#------------------------------#------------------#----------------------------#

           # Allows user to log in, create an account, or watch a video #
                     # Very first screen in the InCollege app #

def login_menu():


# Display Menu

    while True:

        home_.show_success_story()

        print("")
        print("|-----------------------------|")
        print("            Options            ")
        print("|-----------------------------|")
        print("")

        print("  [1] Watch Video Testimonial")
        print("   [2] Log In")
        print("    [3] Create a New Account")
        print("     [4] Find a Friend")
        print("      [5] Quit")
        print("")

        login_choice = input("Enter an option (or press Enter to access links): ")
        print("")


# User Chooses

        if login_choice == "": home_.linkster()
        elif login_choice == "1": home_.watch_video()
        elif login_choice == "2": login()
        elif login_choice == "3": create_account()
        elif login_choice == "4": home_.friend_status()

        elif login_choice == "5":
            print("Quitting the app...")
            exit()


# Error Handling

        else:
            print("Your chosen input is invalid. Please select a number 1-4.")


# End of File
