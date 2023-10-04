
                         ###############################
##############################                     #############################
##############################  D A T A B A S E S  #############################
##############################                     #############################
                         ###############################

                     # All code pertaining to data storage. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3

from config import DBAccounts, DBSettings, DBJobs, DBConnections, DBRequests


                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Database Connection                        #
#                                                                              #
#                             [ 2 ] Table - Accounts                           #
#                             [ 3 ] Table - Settings                           #
#                             [ 4 ] Table - Jobs                               #
#                             [ 5 ] Table - Requests                           #
#                             [ 6 ] Table - Connections                        #
#                                                                              #
#                             [ 7 ] Create All Tables                          #
#                                                                              #
#------------------------------------------------------------------------------#


                    #########################################
#######################  C O N N E C T I O N   S E T U P  ######################
                    #########################################

                   # Functions that connect to each database #

                         #---------------------------#
#------------------------#    Database Connection    #-------------------------#
                         #---------------------------#

       # Connects to passed database address; returns connection and cursor #

def connect_to(database):

    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        return connection, cursor

    except sqlite3.Error as err:
        print("There was an error connecting to the database: ", err)
        return None, None



                              #####################
#################################  T A B L E S  ################################
                              #####################

                  # Functions that create each database table #

                             #----------------------#
#----------------------------#    Accounts Table    #--------------------------#
                             #----------------------#

def create_accounts_table():


    connection, cursor = connect_to(DBAccounts)

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                username VARCHAR(12) PRIMARY KEY,
                password VARCHAR(12),
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                university VARCHAR(100),
                major VARCHAR(50)
            );
        ''')
        connection.commit()

    except sqlite3.Error as err:
        print("There was an error creating the 'accounts' table: ", err)

    finally:

        if connection:
            connection.close()


                             #----------------------#
#----------------------------#    Settings Table    #--------------------------#
                             #----------------------#

def create_settings_table():


    connection, cursor = connect_to(DBSettings)

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                username VARCHAR(12) PRIMARY KEY,
                language VARCHAR(12),
                email_on BOOLEAN,
                sms_on BOOLEAN,
                ads_on BOOLEAN,
                FOREIGN KEY (username) REFERENCES accounts(username),
                CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES accounts(username)
            );
        ''')
        connection.commit()

    except sqlite3.Error as err:
        print("There was an error creating the settings table: ", err)

    finally:

        if connection:
            connection.close()


                               #-----------------#
#------------------------------#    Job Table    #-----------------------------#
                               #-----------------#

def create_job_table():


    connection, cursor = connect_to(DBJobs)

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                job_id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title VARCHAR(250),
                description TEXT,
                location VARCHAR(250),
                employer VARCHAR(100),
                salary DECIMAL(10, 2),
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                FOREIGN KEY (first_name) REFERENCES accounts(first_name),
                FOREIGN KEY (last_name) REFERENCES accounts(last_name),
                -- Add constraint names to avoid confusion
                CONSTRAINT fk_first_name FOREIGN KEY (first_name) REFERENCES accounts(first_name),
                CONSTRAINT fk_last_name FOREIGN KEY (last_name) REFERENCES accounts(last_name)
            );
        ''')
        connection.commit()

    except sqlite3.Error as err:
        print("There was an error creating the 'jobs' table: ", err)

    finally:

        if connection:
            connection.close()

                              # ---------------------#
# ----------------------------#    Requests Table    #--------------------------#
                              # ---------------------#

def create_requests_table():

    connection, cursor = connect_to(DBRequests)

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS requests (
                request_id INTEGER PRIMARY KEY AUTOINCREMENT,
                requester VARCHAR(12),
                recipient VARCHAR(12),
                FOREIGN KEY (requester) REFERENCES accounts(username),
                FOREIGN KEY (recipient) REFERENCES accounts(username),
                CONSTRAINT fk_username FOREIGN KEY (requester) REFERENCES accounts(username),
                CONSTRAINT fk_username FOREIGN KEY (recipient) REFERENCES accounts(username)
            );
        ''')
        connection.commit()

    except sqlite3.Error as err:
        print("There was an error creating the requests table: ", err)

    finally:

        if connection:
            connection.close()

                              # ------------------------#
# ----------------------------#    Connections Table    #--------------------------#
                              # ------------------------#

def create_connections_table():

    connection, cursor = connect_to(DBConnections)

    if connection is None:
        return

    try:
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS connections (
                            connection_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            person1 VARCHAR(12),
                            person2 VARCHAR(12),
                            FOREIGN KEY (person1) REFERENCES accounts(username),
                            FOREIGN KEY (person2) REFERENCES accounts(username),
                            CONSTRAINT fk_username FOREIGN KEY (person1) REFERENCES accounts(username),
                            CONSTRAINT fk_username FOREIGN KEY (person2) REFERENCES accounts(username)
                        );
                    ''')
        connection.commit()

    except sqlite3.Error as err:
        print("There was an error creating the connections table: ", err)

    finally:

        if connection:
            connection.close()

                             #---------------------#
#----------------------------#    Create Tables    #---------------------------#
                             #---------------------#

def create_all_tables():

    create_accounts_table()
    create_settings_table()
    create_job_table()
    create_requests_table()
    create_connections_table()



# End of File
