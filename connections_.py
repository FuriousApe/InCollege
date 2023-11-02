                                #####################
###################################               ##################################
###################################  Connections  ##################################
###################################               ##################################
                                #####################

                      # All code pertaining to connections. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3

import config
import profiles_

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] View Connections                           #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                          #------------------------#
#-------------------------#    View Connections    #---------------------------#
                          #------------------------#

          # Allows a user to view their connections, and delete them.

def menu():

    friends = config.user.get_friends()

    # Print all connections
    if not friends:
        print("\nYou currently have no connections.")
        return

    print("\nYou are connected with these users:")

    for index, (username, created_a_profile) in enumerate(friends, 1):
        if created_a_profile:
            print(f"[{index}] {username}    View Profile [{index + len(friends)}]")
        else:
            print(f"[{index}] {username}")

    print("")
    choice = input("Enter the number for a connection to manage or profile to view: ")

    if not choice.isdigit():
        print("Invalid choice.")
        return

    choice_int = int(choice)

    # Set Bools for input range
    within_connection_range = 1 <= choice_int <= len(friends)
    within_profile_range = len(friends) < choice_int <= 2 * len(friends)

    # User wants to manage a connection
    if within_connection_range:
        selected_friend = friends[choice_int - 1][0]
        print("\nSelect an option to manage this connection:")
        print("[ 1 ] Delete connection\n")

        choice = input("Enter your selection: ")

        if choice == "1":
            # Delete connection
            if config.user.remove_connection(selected_friend):
                print("\nConnection is deleted!\n")
            else:
                print("\nError deleting connection.\n")

    # User wants to view a profile
    elif within_profile_range:
        selected_profile = friends[(choice_int - len(friends)) - 1][0]
        profiles_.display_profile(selected_profile)

    else:
        print("Invalid number.")




# End of file
