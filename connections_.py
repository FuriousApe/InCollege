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

from config import DBRequests
from data_ import connect_to

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Load Connections                           #
#                             [ 2 ] Save Connections                           #
#                             [ 3 ] Delete Connections                         #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                             #----------------------------#
#----------------------------#      Load Connections      #---------------------------#
                             #----------------------------#

            # Gets all connections from requests database, returns them. #

def load_connections():


# Connect to Database

    connection, cursor = connect_to(config.DBConnections)

    if connection is None:
        return


# Define Target Info

    query = '''
        SELECT
            person1,
            person2
        FROM
            connections;
    '''


# Execute Query

    try:
        cursor.execute(query)
        connections_data = cursor.fetchall()
        config.Connections = [{
            "Person1": person1,
            "Person2": person2
        } for person1, person2 in connections_data]

    except sqlite3.Error as err:
        print("There was an error delivering the query: ", err)


# Close Connection

    finally:

        if connection:
            connection.commit()
            connection.close()

            return config.Connections

                               #-----------------------#
#------------------------------#    Save Connection    #------------------------------#
                               #-----------------------#

          # Takes a dict of connection info, uploads it to the connections database #

def save_connection(connect):


# Connect to DB

    connection, cursor = connect_to(config.DBConnections)


# To these Columns...

    query = '''
        INSERT INTO connections (
            person1,
            person2
        )
        VALUES (?, ?);
        '''


# ...Insert this Data from Argument

    try:
        cursor.execute(query,
            (
                connect["Person1"],
                connect["Person2"]
            )
        )

        connection.commit()
        #print("Connection completed!")


# Error Handling

    except sqlite3.Error as err:
        print("There was an error creating the connection: ", err)


# Close Connection

    finally: connection.close()

                               #----------------------#
#------------------------------#    Delete Request    #------------------------------#
                               #----------------------#

          # Takes a dict of connection info, deletes it (both directions) from connections #

def delete_connection(connect):


# Connect to DB

    connection, cursor = connect_to(config.DBConnections)


# To these Columns...

    query = '''
        DELETE FROM connections WHERE person1 = ? AND person2 = ?
        '''


# ...Insert this Data from Argument

    try:
        cursor.execute(query,
            (
                connect["Person1"],
                connect["Person2"]
            )
        )

        connection.commit()
        #print("Connection deleted!")


# Error Handling

    except sqlite3.Error as err:
        print("There was an error deleting the connection: ", err)

# To these Columns...

    query = '''
        DELETE FROM connections WHERE person1 = ? AND person2 = ?
        '''


# ...Insert this Data from Argument

    try:
        cursor.execute(query,
            (
                connect["Person2"],
                connect["Person1"]
            )
        )

        connection.commit()
        #print("Connection deleted!")


# Error Handling

    except sqlite3.Error as err:
        print("There was an error deleting the connection: ", err)


# Close Connection

    finally: connection.close()

                               #-------------------------#
#------------------------------#    View Connections     #------------------------------#
                               #-------------------------#

          # Allows a user to view their connections, and delete them.

def view_connections():

    connections = load_connections()

    # Load result_requests with connections that current user is a part of
    result_connections = []

    for connection in connections:
        if connection["Person1"] == config.User["Username"]:
            result_connections.append(connection)
        elif connection["Person2"] == config.User["Username"]:
            result_connections.append(connection)

    # Print all connections
    print("")
    if not result_connections:
        print("You currently have no connections.")
    else:
        print("You are connected with these users:")

        count = 1
        for connection in result_connections:
            if connection["Person1"] == config.User["Username"]:
                print("[", str(count), "] ", connection["Person2"])
                count += 1
            elif connection["Person2"] == config.User["Username"]:
                print("[", str(count), "] ", connection["Person1"])
                count += 1

        # Let user chose a connection to manage
        print("")
        choice = input("Enter the number for a connection to manage: ")
        if int(choice) < 1 or int(choice) > len(result_connections):
            print("Invalid number.")
            return
        chosen_connection = result_connections[int(choice) - 1]

        print("")
        print("Select an option to manage this connection:")
        print("[ 1 ] Delete connection")
        print("")
        manage = input("Enter your selection: ")


        print("")
        if int(manage) == 1:
            print("Connection is deleted!")

            # Delete connection
            delete_connection(chosen_connection)