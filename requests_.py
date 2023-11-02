                              #####################
###################################            ##################################
###################################  Requests  ##################################
###################################            ##################################
                              #####################

                         # All code pertaining to requests. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3

import config
import connections_

from classes.User import User

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] View incoming requests                     #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                            #----------------------#
#---------------------------#    View Requests     #---------------------------#
                            #----------------------#

     # Allows a user to view and accept their incoming connection requests #

def menu():

    user = config.user
    pending = user.pending_requests()

    # Print incoming requests
    if not pending: print("\nYou have no incoming friend requests.")

    else:
        print("\nThese users have sent you friend requests:")

        count = 1
        for each in pending:
            print("[", str(count), "] ", each.requester)
            count += 1

        # Let user choose a friend request to accept or deny
        choice = input("\nEnter the number for a request to manage: ")
        if not choice.isdigit():
            return
        elif int(choice) < 1 or int(choice) > len(pending):
            print("Invalid number.")
            return

        request = pending[int(choice) - 1]
        friend = User.fetch(request.requester)

        print("\nChoose whether to accept or reject this request:")
        print("[ 1 ] Accept")
        print("[ 2 ] Reject")

        choice = input("\nEnter your selection: ")
        if not choice.isdigit(): return

        if int(choice) == 1:

            user.accept_request(friend)

            print(friend.username, "is now your friend!")


        elif int(choice) == 2:

            user.reject_request(friend)

            print("Request is deleted!")






# End of file
