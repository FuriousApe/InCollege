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

from config import DBRequests
from data_ import connect_to

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Load Requests                              #
#                             [ 2 ] Send Requests                              #
#                             [ 3 ] Delete Requests                            #
#                                                                              #
#                             [ 4 ] View incoming requests                     #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                             #-------------------------#
#----------------------------#      Load Requests      #---------------------------#
                             #-------------------------#

            # Gets all connection requests from requests database, returns them. #

def load_requests():


# Connect to Database

    connection, cursor = connect_to(DBRequests)

    if connection is None:
        return


# Define Target Info

    query = '''
        SELECT
            requester,
            recipient
        FROM
            requests;
    '''


# Execute Query

    try:
        cursor.execute(query)
        requests_data = cursor.fetchall()
        config.Requests = [{
            "Requester": requester,
            "Recipient": recipient
        } for requester, recipient in requests_data]

    except sqlite3.Error as err:
        print("There was an error delivering the query: ", err)


# Close Connection

    finally:

        if connection:
            connection.commit()
            connection.close()

            return config.Requests

                               #--------------------#
#------------------------------#    Save Request    #------------------------------#
                               #--------------------#

          # Takes a dict of request info, uploads it to the request database #

def save_request(request):


# Connect to DB

    connection, cursor = connect_to(DBRequests)


# To these Columns...

    query = '''
        INSERT INTO requests (
            requester,
            recipient
        )
        VALUES (?, ?);
        '''


# ...Insert this Data from Argument

    try:
        cursor.execute(query,
            (
                request["Requester"],
                request["Recipient"]
            )
        )

        connection.commit()
        print("Connection request made!")


# Error Handling

    except sqlite3.Error as err:
        print("There was an error sending the request: ", err)


# Close Connection

    finally: connection.close()

                               #----------------------#
#------------------------------#    Delete Request    #------------------------------#
                               #----------------------#

          # Takes a dict of request info, deletes it from the request database #

def delete_request(request):


# Connect to DB

    connection, cursor = connect_to(DBRequests)


# To these Columns...

    query = '''
        DELETE FROM requests WHERE requester = ? AND recipient = ?
        '''


# ...Insert this Data from Argument

    try:
        cursor.execute(query,
            (
                request["Requester"],
                request["Recipient"]
            )
        )

        connection.commit()
        #print("Connection request deleted!")


# Error Handling

    except sqlite3.Error as err:
        print("There was an error deleting the request: ", err)


# Close Connection

    finally: connection.close()

                               #----------------------#
#------------------------------#    View Requests     #------------------------------#
                               #----------------------#

          # Allows a user to view and accept their incoming connection requests

def view_requests():

    requests = load_requests()

    # Load result_requests with requests that current user is the recipient of
    result_requests = []

    for request in requests:
        if request["Recipient"] == config.User["Username"]:
            result_requests.append(request)

    # Print incoming requests
    print("")
    if not result_requests:
        print("You have no incoming connection requests.")
    else:
        print("These users have sent you connection requests:")

        count = 1
        for request in result_requests:
            print("[", str(count), "] ", request["Requester"])
            count += 1

        # Let user chose a request to accept
        print("")
        choice = input("Enter the number for a request to accept: ")
        chosen_request = result_requests[int(choice) - 1]

        print(request["Requester"], "is now a connection!")

        # Delete request ( request is now a connection )
        delete_request(chosen_request)
