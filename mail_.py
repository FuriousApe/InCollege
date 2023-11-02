
                              #####################
###################################           ##################################
###################################  M A I L  ##################################
###################################           ##################################
                              #####################

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import config
import home_

from classes.User import User
from classes.Message import Message

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ]  Menu                                      #
#                                                                              #
#------------------------------------------------------------------------------#


                               ###################
##################################  I N B O X  #################################
                               ###################

               # A list of functions related to the message system #

                                 #-------------#
#--------------------------------#    Inbox    #-------------------------------#
                                 #-------------#

                      # Displays the student email inbox #

def menu():

    user = config.user

    while True:

        print("\n|===============================================|")
        print("|:::::::::::::::::::  INBOX  :::::::::::::::::::|\n")
        user.view_inbox()
        print("\n|-----------------------------------------------|")
        print("   [1] Read a message")
        print("    [2] Send a message")
        print("     [3] View friends")
        if user.plus: print("      [4] View All Members")
        print("\n   [<] Return")

        choice = input("\nChoose an option (or press Enter to access links): ")

        if choice == "": home_.linkster()
        elif choice == "<": return

        # Read a message
        elif choice == "1":

            num = input("Enter the number of the message to read: ")
            if num == "": continue

            try:
                num = int(num)
                if 0 < num <= len(user.inbox):
                    message = user.inbox[num - 1]
                    them = User.fetch(message.sender)

                    user.read_message(message)

                    if input("Do you want to reply to this message? (Y/N) ").upper() == "Y":
                        subject = "Re: " + message.subject
                        content = input("Enter your reply: ")
                        user.send_message(them, subject, content)

            except ValueError:
                print("Invalid choice.")

        # Send a message
        elif choice == "2":

            their_username = input("Enter the recipient's username: ")

            if user.plus or their_username in user.friends:

                them = User.fetch(their_username)

                if not them:
                    print("There was a problem fetching the friend from the database.")
                    return

                subject = input("Enter the subject: ")
                body = input("Enter the content: ")
                user.send_message(them, subject, body)

            else: print("Only Plus members can send messages to non-friends!")

        # View all friends
        elif choice == "3":

            user.view_friends()
            friend_number = input("Select a friend number to send a message or Enter to return: ")

            if friend_number == "": continue

            try:
                friend_number = int(friend_number)
                if 0 < friend_number <= len(user.friends):

                    their_username = user.friends[friend_number - 1]
                    them = User.fetch(their_username)

                    subject = input("Enter the subject: ")
                    body = input("Enter the content: ")
                    user.send_message(them, subject, body)

            except ValueError:
                print("Invalid choice.")

        # View all members (only for Plus members)
        elif choice == "4" and user.plus:

            members = User.all_usernames()

            for index, member in enumerate(members, start=1):
                print(f"[{index}] {member}")

            member_number = input("\nSelect a member number to send a message or Enter to return: ")

            if member_number == "": continue

            try:
                member_number = int(member_number)
                if 0 < member_number <= len(members):

                    their_username = members[member_number - 1]
                    them = User.fetch(their_username)

                    subject = input("Enter the subject: ")
                    body = input("Enter the content: ")
                    user.send_message(them, subject, body)

            except ValueError:
                print("\nInvalid choice.")

        # Handle Wrong Input
        else: print("Invalid input. Please enter an available option.")







# End of file
