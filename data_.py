
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
import config



                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Student Connection                         #
#                             [ 2 ] Job Connection                             #
#                             [ 3 ] Student Table                              #
#                             [ 4 ] Job Table                                  #
#                                                                              #
#------------------------------------------------------------------------------#


                    #########################################
#######################  C O N N E C T I O N   S E T U P  ######################
                    #########################################

                   # Functions that connect to each database #

                          #--------------------------#
#-------------------------#    Student Connection    #-------------------------#
                          #--------------------------#

         # Connects to student database; returns connection and cursor #
             # Called when creating trying to access student info #

def accounts_connect():

    try:
        connection = sqlite3.connect(config.DBAccounts)
        cursor = connection.cursor()
        return connection, cursor

    except sqlite3.Error as err:
        print("There was an error connecting to the student database: ", err)
        return None, None


                            #----------------------#
#---------------------------#    Job Connection    #---------------------------#
                            #----------------------#

          # Connects to job database; returns connection and cursor #
              # Called when creating trying to access job info #

def jobs_connect():

    try:
        connection = sqlite3.connect(config.DBJobs)
        cursor = connection.cursor()
        return connection, cursor

    except sqlite3.Error as err:
        print("There was an error connecting to the job database: ", err)
        return None, None




                              #####################
#################################  T A B L E S  ################################
                              #####################

                  # Functions that create each database table #

                             #---------------------#
#----------------------------#    Student Table    #---------------------------#
                             #---------------------#

def create_student_table():


    connection, cursor = accounts_connect()

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                username VARCHAR(12) PRIMARY KEY,
                password VARCHAR(12),
                first_name VARCHAR(50),
                last_name VARCHAR(50)
            );
        ''')
        connection.commit()

    except sqlite3.Error as err:
        print("There was an error creating the 'accounts' table: ", err)

    finally:

        if connection:
            connection.close()


                               #-----------------#
#------------------------------#    Job Table    #-----------------------------#
                               #-----------------#

def create_job_table():


    connection, cursor = jobs_connect()

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
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



# End of File
