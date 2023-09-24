
                    #########################################
#########################                               ########################
#########################  U S E R   F U N C T I O N S  ########################
#########################                               ########################
                    #########################################

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import config

import jobs_
import skills_
import accounts_

from data_ import accounts_connect


                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Success Story                              #
#                             [ 2 ] Watch Video                                #
#                             [ 3 ] Friend Status                              #
#                             [ 4 ] Connect to a friend                        #
#                             [ 5 ] Home Screen                                #
#                                                                              #
#------------------------------------------------------------------------------#


                               ###################
##################################  L O G I N  #################################
                               ###################

              # A list of functions related to the log-in process #

                             #---------------------#
#----------------------------#    Success Story    #---------------------------#
                             #---------------------#

                      # Displays a student success story #
                    # Called at beginning of login_menu() *

def show_success_story():


    print("")
    print("|-----------------------|")
    print("  Welcome to InCollege!  ")
    print("|-----------------------|")
    print("")
    print("  'When I needed to find a job")
    print("   after finishing school, all of")
    print("   my friends made it seem impossible.")
    print("   But that's when InCollege made all")
    print("   the difference. Now I have my dream job,")
    print("   and now I know that dreams really do come true.'")
    print("                     - Jane Witherby Smith")



                              #-------------------#
#-----------------------------#    Watch Video    #----------------------------#
                              #-------------------#

                    # Menu for watching a video testimonial #
                     # One of the paths from login_menu() #

def watch_video():


    print("")
    print("|---------------------------------|")
    print("  Jane Smith's Incredible Journey  ")
    print("|---------------------------------|")
    print("")
    print("  [1] Play Video")
    print("   [2] Return")
    print("")

    vid_choice = input("Enter an option (1 or 2): ")
    print("")

    if vid_choice == "1":

        print("|---------------------------------|")
        print("|                                 |")
        print("|                                 |")
        print("|       Video is now playing      |")
        print("|                                 |")
        print("|                                 |")
        print("|---------------------------------|")

    elif vid_choice == "2":
        return

    else:
        print("Your chosen input is invalid. Please select a number 1 or 2.")



                             #---------------------#
#----------------------------#    Friend Status    #---------------------------#
                             #---------------------#

         # Returns account status of user-specified first and last name #
                     # One of the paths from login_menu() #

def friend_status():


    print("")
    print("Who would you like to find?: ")
    print("")


# Get Input

    first_name = input("First Name: ").strip().lower()
    last_name = input("Last Name: ").strip().lower()

    friend = accounts_.find_account(first_name, last_name)


# Print Result

    if friend: print("They are a part of the InCollege system.")
    else: print("They are not a part of the InCollege system yet.")



                          #-------------------------#
#-------------------------#    Connect to Friend    #--------------------------#
                          #-------------------------#

              # Allows user to connect to a friend in the system #
                      # One of the paths from home() #

def connect():


    print("")
    print("|-------------------|")
    print("  InCollege Connect  ")
    print("|-------------------|")
    print("")

    print("Who would you like to find?")
    print("")


# Get Input

    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    friend = accounts_.find_account(first_name, last_name)


# If Friend 'is' User

    if friend == config.User and friend is not None:
        print(friend)
        print("")
        print("That's you, silly!")
        print("")

        return



# Results

    if friend:

        print("")
        print("Looks like they're in the system!")
        print("")
        print("Here's their contact info:")
        print("--------------------------")

        print(friend["First Name"], friend["Last Name"])
        print("Username:", friend["Username"])
        print("")

    else:

        print("")
        print("This person is not in the system yet.")
        print("")



                           ###########################
##############################  M A I N   M E N U  #############################
                           ###########################

          # Provides routes to other menus : jobs, contacts, and skills #
                  # The screen the user sees after logging in #

#------------------------------#-------------------#---------------------------#
#------------------------------#    Home Screen    #---------------------------#
#------------------------------#-------------------#---------------------------#

def home():


# Display Menu

    while True:

        print("")
        print("Logged in as", config.User["First Name"], config.User["Last Name"])
        print("")
        print("|-------------|")
        print("  Home Screen  ")
        print("|-------------|")
        print("")

        print("  [1] Job Search / Internship")
        print("   [2] Find Someone You Know")
        print("    [3] Learn a New Skill")
        print("     [4] Log Out")
        print("")


# User Chooses

        main_choice = input("Enter an option (1-4): ")

        if main_choice == "1":
            jobs_.job_menu()

        elif main_choice == "2":
            connect()

        elif main_choice == "3":
            skills_.skill_menu()

        elif main_choice == "4":
            print("Logging out...")
            return

        else:
            print("Invalid choice. Please select a number 1-4.")



# End of File
