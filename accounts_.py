
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
import profiles_
from data_ import connect_to_database

from classes.User import User
from classes.UserSettings import UserSettings
from classes.UserProfile import UserProfile


                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Password Requirements                      #
#                             [ 2 ] Create Account                             #
#                                                                              #
#                             [ 3 ] Log In                                     #
#                             [ 4 ] Log Out                                    #
#                             [ 5 ] Login Menu                                 #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

          # All functions that deal with the login process are here. #

                          #---------------------------#
#-------------------------#   Password Requirements   #------------------------#
                          #---------------------------#

                # Checks password argument against requirements #

def password_requirements(password):

    if (
        config.PasswordMinLength > len(password)
        or config.PasswordMaxLength < len(password)
        or not any(c.isupper() for c in password)
        or not any(c.isdigit() for c in password)
        or not any(c.isascii()
        and not c.isalnum() for c in password)
    ):
        return False

    else: return True


                            #----------------------#
#---------------------------#    Create Account    #---------------------------#
                            #----------------------#

          # Gets user info, checks requirements, saves them to database #

def create_account():

    if not User.has_room_for_new_account():
        return

    # Nested function for retrieving input
    def get_input(prompt, error_message, transform_func=None):
        while True:
            value = input(prompt)
            if not value:
                print("\n" + error_message + "\n")
                continue
            if transform_func:
                value = transform_func(value)
            return value

    print("\n|----------------------------|")
    print("       Account Creation       ")
    print("|----------------------------|\n")

    # Entering Personal Info
    first_name = get_input("First Name: ", "You must enter your first name to continue.")
    last_name = get_input("Last Name: ", "You must enter your last name to continue.")
    university = get_input("University: ", "You must enter your university to continue.", config.capitalize_each_word)
    major = get_input("Major: ", "You must enter your major to continue.", config.capitalize_each_word)

    # Creating a Username
    while True:
        username = input("Enter a username: ")
        if not username:
            print("You must enter a username.")
            continue
        if not User.username_exists(username):
            break
        print("This username already exists. Please choose a different one.")

    # Creating a Password
    while True:
        password = input("Enter a password: ")
        if password_requirements(password):
            break
        print("-------------------------------")
        print("Invalid password. Requirements:")
        print("   [*] Character length: 8-12")
        print("   [*] Must contain at least 1 uppercase letter")
        print("   [*] Must contain at least 1 digit")
        print("   [*] Must contain at least 1 special character")

    # Choosing regular or plus account type
    print("Would you like to create a plus account?")
    print("Plus accounts cost a fee of $10 per month.")

    plus = get_input("Enter Yes/No: ", "Invalid entry. Must be Yes/No.", lambda x: x.lower())

    plus = True if plus == "yes" else False



    # :::::::::::::::::  CurrentUser is now an object  ::::::::::::::::: #
    #          and we can call User methods directly on the user         #

    # This saves to config and database simultaneously
    config.user = User.create(username = username,
                                     password = password,
                                     first_name = first_name,
                                     last_name = last_name,
                                     university = university,
                                     major = major,
                                     created_a_profile = False,
                                     plus = plus)

    # Same for default settings / starter profile
    config.settings = config.user.get_settings()
    config.profile = config.user.get_profile()

    print("\nAccount created successfully.\n")

    # Profile Creation
    while True:
        choice = input("\nSince you're here, would you like to create your profile? (Y/N):")
        print("")

        choice.upper()

        if choice == 'Y':
            profiles_.edit_profile()
            break

        elif choice == 'N':
            print("No problem! You can create your profile at any time from the Home Screen.")
            break

        else:
            print("Invalid input. Please enter either Y (for yes) or N (for no).")



                                 #-------------#
#--------------------------------#    Login    #-------------------------------#
                                 #-------------#

   # Performs the login function, accepts or rejects the username/password #

def login():

    # Get Credentials
    while True:

        username = input("Username: ")
        password = input("Password: ")

        # Cross-check
        is_valid = User.validate_credentials(username, password)

        # Outcomes
        if is_valid:

            print("You have successfully logged in.")

            config.user = User.fetch(username)
            config.settings = UserSettings.fetch(username)
            config.profile = UserProfile.fetch(username)

            home_.home()

            return

        else:
            print("")
            print("X------------X------------X------------X------------X")
            print("|   Incorrect username/password, please try again.  |")
            print("X------------X------------X------------X------------X")
            print("")

            choice = input('''
                Press 'Enter' now to try again or
                any other key to return to the opening menu:
                ''')

            if choice: return


                                 #--------------#
#--------------------------------#    Logout    #------------------------------#
                                 #--------------#

            # Logs the user out; resets all global variables to default #

def logout():

    config.user = None
    config.profile = None
    config.settings = None



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

        choice = input("Enter an option (or press Enter to access links): ")
        print("")

        # User Chooses
        if choice == "": home_.linkster()
        elif choice == "1": home_.watch_video()
        elif choice == "2": login()
        elif choice == "3": create_account()
        elif choice == "4": home_.friend_status()

        elif choice == "5":
            print("Quitting the app...")
            exit()

        # Error Handling
        else:
            print("Your chosen input is invalid. Please select a number 1-4.")


# End of File
