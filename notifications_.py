                                #####################
###################################                ##################################
###################################  Notificatios  ##################################
###################################                ##################################
                                #####################

                         # All code pertaining to connections. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3

import config
import accounts_
import profiles_

from data_ import connect_to

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Load Notifications                         #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                             #------------------------------#
#----------------------------#      Load Notifications      #---------------------------#
                             #------------------------------#

            # Gets all users with from notifications database, returns them. #

def load_notifications():

    # Connect to Database

    connection, cursor = connect_to(config.DBNotifications)

    if connection is None:
        return

    try:
        # Fetch users who have recently had an applied job deleted
        cursor.execute('''
            SELECT student_username FROM notifications
        ''')
        usernames = cursor.fetchall()

        return usernames
    except sqlite3.Error as err:
        print("There was an error delivering the query: ", err)


    # Close Connection

    finally:

        if connection:
            connection.commit()
            connection.close()