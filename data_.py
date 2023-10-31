
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

from config import (
    DBAccounts,
    DBProfiles,
    DBSettings,
    DBJobs,
    DBSavedJobs,
    DBApplications,
    DBConnections,
    DBRequests, DBNotifications
)


                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Database Connection                        #
#                                                                              #
#                             [ 2 ] Table - Accounts                           #
#                             [ 3 ] Table - Profiles                           #
#                             [ 4 ] Table - Settings                           #
#                                                                              #
#                             [ 5 ] Table - Jobs                               #
#                             [ 6 ] Table - Saved Jobs                         #
#                             [ 7 ] Table - Applications                       #
#                             [ 8 ] Table - Notifications                      #
#                                                                              #
#                             [ 9 ] Table - Requests                           #
#                             [ 10 ] Table - Connections                       #
#                                                                              #
#                             [ 11 ] Create All Tables                         #
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
        #connection.execute("PRAGMA foreign_keys = ON;")
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
                major VARCHAR(50),
                created_a_profile BOOLEAN,
                plus BOOLEAN
            );
        ''')
        connection.commit()

    except sqlite3.Error as err:
        print("There was an error creating the 'accounts' table: ", err)

    finally:

        if connection: connection.close()


                             #----------------------#
#----------------------------#    Profiles Table    #--------------------------#
                             #----------------------#

def create_profiles_table():

    connection, cursor = connect_to(DBProfiles)

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
                username VARCHAR(12) PRIMARY KEY,
                title TEXT,
                about TEXT,

                job_1_title TEXT,
                job_1_employer TEXT,
                job_1_date_started DATE,
                job_1_date_ended DATE,
                job_1_location TEXT,
                job_1_description TEXT,

                job_2_title TEXT,
                job_2_employer TEXT,
                job_2_date_started DATE,
                job_2_date_ended DATE,
                job_2_location TEXT,
                job_2_description TEXT,

                job_3_title TEXT,
                job_3_employer TEXT,
                job_3_date_started DATE,
                job_3_date_ended DATE,
                job_3_location TEXT,
                job_3_description TEXT,

                college_name VARCHAR(100),
                college_major VARCHAR(50),
                college_years_attended TEXT,

                FOREIGN KEY (username) REFERENCES accounts(username),
                FOREIGN KEY (college_name) REFERENCES accounts(university),
                FOREIGN KEY (college_major) REFERENCES accounts(major),

                CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES accounts(username),
                CONSTRAINT fk_college_name FOREIGN KEY (college_name) REFERENCES accounts(university),
                CONSTRAINT fk_college_major FOREIGN KEY (college_major) REFERENCES accounts(major)
            );
        ''')
        connection.commit()

    except sqlite3.Error as err:
        print("There was an error creating the profiles table: ", err)

    finally:

        if connection: connection.close()


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

        if connection: connection.close()


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
                username VARCHAR(12),
                -- Add constraint name to avoid confusion
                CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES accounts(username)
            );
        ''')
        connection.commit()

    except sqlite3.Error as err:
        print("There was an error creating the 'jobs' table: ", err)

    finally:

        if connection: connection.close()



                           #------------------------#
#--------------------------#    Saved Jobs Table    #--------------------------#
                           #------------------------#

def create_saved_jobs_table():

    connection, cursor = connect_to(DBSavedJobs)

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saved_jobs (
                student_username VARCHAR(12),
                job_id INTEGER,
                CONSTRAINT fk_student_username FOREIGN KEY (student_username) REFERENCES accounts(username),
                CONSTRAINT fk_job_id FOREIGN KEY (job_id) REFERENCES jobs(job_id)
            );
        ''')
        connection.commit()


    except sqlite3.Error as err:

        print("There was an error creating the 'saved_jobs' table: ", err)


    finally:

        if connection: connection.close()



                          #--------------------------#
#-------------------------#    Applications Table    #-------------------------#
                          #--------------------------#

def create_applications_table():

    connection, cursor = connect_to(DBApplications)

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applications (
                application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_username VARCHAR(12),
                job_id INTEGER,
                graduation_date DATE,
                start_date DATE,
                application_text TEXT,
                CONSTRAINT fk_student_username FOREIGN KEY (student_username) REFERENCES accounts(username),
                CONSTRAINT fk_job_id FOREIGN KEY (job_id) REFERENCES jobs(job_id)
            );
        ''')
        connection.commit()


    except sqlite3.Error as err:

        print("There was an error creating the 'applications' table: ", err)


    finally:

        if connection: connection.close()

                            # --------------------------#
# --------------------------#    Notifications Table    #--------------------------#
                            # --------------------------#

def create_notifications_table():

    connection, cursor = connect_to(DBNotifications)

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notifications (
                student_username VARCHAR(12),
                CONSTRAINT fk_student_username FOREIGN KEY (student_username) REFERENCES accounts(username)
            );
        ''')
        connection.commit()


    except sqlite3.Error as err:

        print("There was an error creating the 'notifications' table: ", err)


    finally:

        if connection: connection.close()



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

        if connection: connection.close()

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

        if connection: connection.close()

                             #---------------------#
#----------------------------#    Create Tables    #---------------------------#
                             #---------------------#

def create_all_tables():

    create_accounts_table()
    create_profiles_table()
    create_settings_table()
    create_job_table()
    create_applications_table()
    create_notifications_table()
    create_saved_jobs_table()
    create_requests_table()
    create_connections_table()



# End of File
