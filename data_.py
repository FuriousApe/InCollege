
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
from config import DB


                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Database Connection                        #
#                                                                              #
#                             [ 2 ] Table - Users                              #
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

def connect_to_database():

    try:
        connection = sqlite3.connect(DB)
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        return connection, cursor

    except sqlite3.Error as err:
        print("There was an error connecting to the database: ", err)
        return None, None



                              #####################
#################################  T A B L E S  ################################
                              #####################

                  # Functions that create each database table #

                              #-------------------#
#-----------------------------#    Users Table    #----------------------------#
                              #-------------------#

def create_users_table():


    connection, cursor = connect_to_database()

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
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
        print("There was an error creating the 'users' table: ", err)

    finally:

        if connection: connection.close()


                             #----------------------#
#----------------------------#    Profiles Table    #--------------------------#
                             #----------------------#

def create_profiles_table():

    connection, cursor = connect_to_database()

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

                university VARCHAR(100),
                major VARCHAR(50),
                years_attended TEXT,

                CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES users(username)
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


    connection, cursor = connect_to_database()

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
                CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES users(username)
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


    connection, cursor = connect_to_database()

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
                CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES users(username)
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

    connection, cursor = connect_to_database()

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saved_jobs (
                username VARCHAR(12),
                job_id INTEGER,
                CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES users(username),
                CONSTRAINT fk_job_id FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE
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

    connection, cursor = connect_to_database()

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applications (
                application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(12),
                job_id INTEGER,
                graduation_date DATE,
                start_date DATE,
                application_text TEXT,
                CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES users(username),
                CONSTRAINT fk_job_id FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE
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

    connection, cursor = connect_to_database()

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notifications (
                notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(12),
                message TEXT,
                seen BOOLEAN DEFAULT FALSE,
                CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES users(username)
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

    connection, cursor = connect_to_database()

    if connection is None:
        return

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS requests (
                request_id INTEGER PRIMARY KEY AUTOINCREMENT,
                requester VARCHAR(12),
                recipient VARCHAR(12),
                CONSTRAINT fk_username FOREIGN KEY (requester) REFERENCES users(username),
                CONSTRAINT fk_username FOREIGN KEY (recipient) REFERENCES users(username)
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

    connection, cursor = connect_to_database()

    if connection is None:
        return

    try:
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS connections (
                            connection_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            person1 VARCHAR(12),
                            person2 VARCHAR(12),
                            CONSTRAINT fk_username FOREIGN KEY (person1) REFERENCES users(username),
                            CONSTRAINT fk_username FOREIGN KEY (person2) REFERENCES users(username)
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

    create_users_table()
    create_profiles_table()
    create_settings_table()
    create_job_table()
    create_applications_table()
    create_notifications_table()
    create_saved_jobs_table()
    create_requests_table()
    create_connections_table()



# End of File
