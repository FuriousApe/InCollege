
                    #########################################
#########################                               ########################
#########################  U S E R   F U N C T I O N S  ########################
#########################                               ########################
                    #########################################

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import config
import policies_
import jobs_
import skills_
import accounts_

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Success Story                              #
#                             [ 2 ] Watch Video                                #
#                                                                              #
#                             [ 3 ] Friend Status                              #
#                             [ 4 ] Connect to a friend                        #
#                             [ 5 ] Search by last name                        #
#                             [ 6 ] Search by university                       #
#                             [ 7 ] Search by major                            #
#                                                                              #
#                             [ 8 ] Home Screen                                #
#                                                                              #
#                             [ 9 ] Useful Links                               #
#                             [ 10 ] InCollege Important Links                 #
#                             [ 11 ] General Links                             #
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
    print("|----------------------------|")
    print("     Welcome to InCollege!    ")
    print("|----------------------------|")
    print("")
    print("  'When I needed to find a job")
    print("   after finishing school, all of")
    print("   my friends made it seem impossible.")
    print("   But that's when InCollege made all")
    print("   the difference. Now I have my dream job,")
    print("   and now I know that dreams really do come true.'")
    print("                     - Jane Withers Smith")



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

def friend_connect():


    print("")
    print("|-----------------------------|")
    print("       InCollege Connect       ")
    print("|-----------------------------|")
    print("")

    print("How would you like to search?")
    print("[1] Search by last name")
    print("[2] Search by university")
    print("[3] Search by major")

    search_choice = input("Enter an option: ")
    print("")

    # User Chooses

    if search_choice == "1":
        search_lname()
    elif search_choice == "2":
        search_university()
    elif search_choice == "3":
        search_major()

def search_lname():

    accounts = accounts_.load_accounts()

    print("")
    lname = input("Enter a last name to search by: ")
    lname = lname.strip().lower()
    print("")

    result_accounts = []

    for account in accounts:
        if lname in account["Last Name"].strip().lower() and account != config.User:
            result_accounts.append(account)

    if not result_accounts:
        print("")
        print("No accounts found.")
    else:
        print("")
        count = 1
        for account in result_accounts:
            print("[", str(count), "] ", account["First Name"], account["Last Name"])
            count += 1

        print("")
        choice = input("Enter the number for a student to send a connection request: ")


def search_university():
    accounts = accounts_.load_accounts()

    print("")
    university = input("Enter a university to search by: ")
    university = university.strip().lower()
    print("")

    result_accounts = []

    for account in accounts:
        if university in account["University"].strip().lower() and account != config.User:
            result_accounts.append(account)

    if not result_accounts:
        print("")
        print("No accounts found.")
    else:
        print("")
        count = 1
        for account in result_accounts:
            print("[", str(count), "] ", account["First Name"], account["Last Name"])
            count += 1

        print("")
        choice = input("Enter the number for a student to send a connection request: ")

def search_major():
    accounts = accounts_.load_accounts()

    print("")
    major = input("Enter a major to search by: ")
    major = major.strip().lower()
    print("")

    result_accounts = []

    for account in accounts:
        if major in account["Major"].strip().lower() and account != config.User:
            result_accounts.append(account)

    if not result_accounts:
        print("")
        print("No accounts found.")
    else:
        print("")
        count = 1
        for account in result_accounts:
            print("[", str(count), "] ", account["First Name"], account["Last Name"])
            count += 1

        print("")
        choice = input("Enter the number for a student to send a connection request: ")



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
        print("|---------------------------|")
        print("         Home Screen         ")
        print("|---------------------------|")
        print("")

        print("  [1] Job Search / Internship")
        print("   [2] Find Someone You Know")
        print("    [3] Learn a New Skill")
        print("     [4] Log Out")
        print("")


# User Chooses

        main_choice = input("Enter an option (or press Enter to access links): ")

        if main_choice == "": linkster()
        elif main_choice == "1": jobs_.job_menu()
        elif main_choice == "2": friend_connect()
        elif main_choice == "3": skills_.skill_menu()

        elif main_choice == "4":
            print("Logging out...")
            accounts_.logout()
            return

# Error Handling

        else:
            print("Invalid choice. Please select a number 1-4.")



                            #########################
###############################  L I N K S T E R  ##############################
                            #########################

                # Gives the user an easy way to navigate the app #
                   # Available at the bottom of every screen #

#------------------------------#----------------#------------------------------#
#------------------------------#    Linkster    #------------------------------#
#------------------------------#----------------#------------------------------#

def linkster():

    while True:


# Display Menu

        print("")
        print("_________")
        print("  Links |_____________________________________________")
        print(" [<] InCollege Important Links   |   Useful Links [>] ")


# Prompt

        stay_in_menu = True
        link_choice = input("Please select an option (or press Enter to return): ")


# Outcomes

        if link_choice == '': return
        elif link_choice == '<': stay_in_menu = linkster_important()
        elif link_choice == '>': stay_in_menu = linkster_useful()


# Error Handling

        else:
            print("Invalid input. Please enter an available option.")


# Return From Next Menus

        if stay_in_menu: continue
        else: return



                      #---------------------------------#
#---------------------#    InCollege Important Links    #----------------------#
                      #---------------------------------#

def linkster_important():

    while True:


# Signed In?

        if config.User is None: signed_in = False
        else: signed_in = True


# Display Links

        print("")
        print("_____________________________")
        print("  InCollege Important Links |_________________________")
        print(" [a] Copyright Notice       |    [f] Cookie Policy ")
        print(" [b] About                  |    [g] Copyright Policy ")
        print(" [c] Accessibility          |    [h] Brand Policy ")


# Signed In Shows Languages

        if signed_in:
            print(" [d] User Agreement         |    [i] Languages ")
        else:
            print(" [d] User Agreement         |                  ")


# Finish Displaying & Prompt

        print(" [e] Privacy Policy         |                    ")
        print("                                          Go Back [>] ")

        stay_in_menu = True
        important_choice = input("Please select an option (or press Enter to return): ")


# Outcomes

        if important_choice == "": return False
        elif important_choice == '>': return True

        elif important_choice == 'a': stay_in_menu = policies_.notice()
        elif important_choice == 'b': stay_in_menu = policies_.about()
        elif important_choice == 'c': stay_in_menu = policies_.accessibility()
        elif important_choice == 'd': stay_in_menu = policies_.user_agreement()
        elif important_choice == 'e': stay_in_menu = policies_.privacy()
        elif important_choice == 'f': stay_in_menu = policies_.cookies()
        elif important_choice == 'g': stay_in_menu = policies_.copy_right()
        elif important_choice == 'h': stay_in_menu = policies_.brand()
        elif important_choice == 'i' and signed_in: stay_in_menu = policies_.languages()


# Error Handling

        else:
            print("Invalid input. Please enter an available option.")


# Return From Next Menus

        if stay_in_menu: continue
        else: return False



                             #--------------------#
#----------------------------#    Useful Links    #----------------------------#
                             #--------------------#

def linkster_useful():

    while True:


# Display Menu

        print("")
        print("________________")
        print("  Useful Links |______________________________________")
        print(" [a] General              |    [c] Business Solutions ")
        print(" [b] Browse InCollege     |    [d] Directories        ")
        print(" [<] Go Back")


# Prompt

        stay_in_menu = True
        useful_choice = input("Please select an option (or press Enter to return): ")


# Outcomes

        if useful_choice == "": return False
        elif useful_choice == '<': return stay_in_menu

        elif useful_choice == 'a': stay_in_menu = linkster_general()
        elif useful_choice == 'b': config.under_construction()
        elif useful_choice == 'c': config.under_construction()
        elif useful_choice == 'd': config.under_construction()


# Error Handling

        else:
            print("Invalid input. Please enter an available option.")


# Return from Next Menus

        if stay_in_menu: continue
        else: return False



                               #---------------#
#------------------------------#    General    #-------------------------------#
                               #---------------#

                # Under 'Useful Links' - shows many more links #

def linkster_general():

    while True:


# Signed In?

        if config.User is None: signed_in = False
        else: signed_in = True


# Display Menu

        print("")
        print("___________")
        print("  General |___________________________________________")
        print(" [a] Help Center            |    [d] Blog             ")
        print(" [b] About                  |    [e] Careers          ")
        print(" [c] Press                  |    [f] Developers       ")
        print("")


# Signed Out Shows 'Sign Up'

        if signed_in:
            print(" [<] Go Back")
        else:
            print(" [<] Go Back                              Sign Up [>] ")



# Prompt

        general_choice = input("Please select an option (or press Enter to return): ")


# Outcomes

        if general_choice == "": return False
        elif general_choice == '<': return True
        elif general_choice == '>' and not signed_in:
            accounts_.login_menu()
            return False


        elif general_choice == 'a':
            print("\nWe're here to help.\n")

        elif general_choice == 'b':
            print("\nInCollege:")
            print("   The world's largest college student network")
            print("   with many users in many countries and territories worldwide.\n")

        elif general_choice == 'c':
            print("\nInCollege Pressroom:")
            print("   Stay on top of the latest news, updates, and reports.\n")


        elif general_choice == 'd': config.under_construction()
        elif general_choice == 'e': config.under_construction()
        elif general_choice == 'f': config.under_construction()


# Error Handling

        else:
            print("Invalid input. Please enter an available option.")



# End of File
