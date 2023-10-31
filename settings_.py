
                          #############################
###############################                   ##############################
###############################  S E T T I N G S  ##############################
###############################                   ##############################
                          #############################

                     # All code the pertains to user settings. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3

import config
import profiles_

from config import DBSettings
from data_ import connect_to

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Initialize Account                         #
#                                                                              #
#                             [ 2 ] Load User Settings                         #
#                             [ 3 ] Save User Settings                         #
#                                                                              #
#                             [ 4 ] Load All Settings                          #
#                             [ 5 ] Save All Settings                          #
#                                                                              #
#                             [ 6 ] Toggle Setting                             #
#                             [ 7 ] Change Language                            #
#                                                                              #
#                             [ 8 ] Guest Controls                             #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                          #--------------------------#
#-------------------------#    Initialize Account    #-------------------------#
                          #--------------------------#

                  # Adds a specified user's default settings #
                       # Also adds empty profile fields #

def initialize_user(username):


# Create Default Settings / Empty Profile

    config.UserSettings = {
                            "Username": username,
                            "Language": "English",
                            "Email On": True,
                            "SMS On": True,
                            "Ads On": True
                            }

# Update Settings

    load_all_settings()
    if config.Settings is None: config.Settings = []
    config.Settings.append(config.UserSettings)
    save_all_settings()



                         #---------------------------#
#------------------------#    Initialize Database    #-------------------------#
                         #---------------------------#

               # Sets all settings of all unset users to default #
                       # Keeps database from being empty #

def initialize_settings_database():


# Load Settings Database

    load_all_settings()


# Check That Each Account Has Settings

    for account in config.Accounts:
        settings_exist = False
        for settings in config.Settings:
            if account["Username"] == settings["Username"]:
                settings_exist = True
                break
        if settings_exist: continue


# If Non-Existent, Add Them

        else:
            initialize_user(account["Username"])



                           #--------------------------#
#--------------------------#    Load User Settings    #------------------------#
                           #--------------------------#

         # Copies user's settings from database into config.UserSettings #
                             # Called during login #

def load_user_settings():


# Connect to the Database

    try:
        config.Connection, cursor = connect_to(DBSettings)

        if config.Connection is None:
            return


# Form the Query

        query = '''
            SELECT
                username,
                language,
                email_on,
                sms_on,
                ads_on
            FROM
                settings
            WHERE
                username = ?;
        '''


# Execute the Query (based on active username)

        cursor.execute(query, (config.User['Username'],))
        user_settings = cursor.fetchone()

        if user_settings is None:
            initialize_user(config.User['Username'])

        else:
            config.UserSettings = {
                            "Username": user_settings[0],
                            "Language": user_settings[1],
                            "Email On": user_settings[2],
                            "SMS On": user_settings[3],
                            "Ads On": user_settings[4]
                            }


# Error Handling

    except sqlite3.Error as err:
        print("There was an error retrieving user settings: ", err)


# Close the Connection

    finally:
        if config.Connection:
            config.Connection.commit()
            config.Connection.close()



                           #--------------------------#
#--------------------------#    Save User Settings    #------------------------#
                           #--------------------------#

              # Saves settings from config.UserSettings to database #

def save_user_settings():


# Connect to Database

    connection, cursor = connect_to(DBSettings)

    if connection is None:
        return


# Define Query

    query = '''
        UPDATE
            settings
        SET
            language = ?,
            email_on = ?,
            sms_on = ?,
            ads_on = ?
        WHERE
            username = ?;
    '''

    try:

# Execute Query

        cursor.execute(query,
            (
            config.UserSettings['Language'],
            config.UserSettings['Email On'],
            config.UserSettings['SMS On'],
            config.UserSettings['Ads On'],
            config.UserSettings['Username']
            )
        )

        connection.commit()


# Update Global Settings

        for user in config.Settings:
            if user['Username'] == config.UserSettings['Username']:
                user['Language'] = config.UserSettings['Language']
                user['Email On'] = config.UserSettings['Email On']
                user['SMS On'] = config.UserSettings['SMS On']
                user['Ads On'] = config.UserSettings['Ads On']


# Error Handling

    except sqlite3.Error as err:
        print("There was an error updating user settings: ", err)


# Closure

    finally:

        if connection:
            connection.close()



                           #-------------------------#
#--------------------------#    Load All Settings    #-------------------------#
                           #-------------------------#

             # Loads all settings of all users into config.Settings #

def load_all_settings():


# Connect to Database

    connection, cursor = connect_to(DBSettings)

    if connection is None:
        return


# Define Query

    query = '''
        SELECT
            username,
            language,
            email_on,
            sms_on,
            ads_on
        FROM
            settings;
    '''


# Execute Query

    try:
        cursor.execute(query)
        settings_data = cursor.fetchall()
        config.Settings = [{
                    "Username": username,
                    "Language": language,
                    "Email On": email_on,
                    "SMS On": sms_on,
                    "Ads On": ads_on
                    } for username, language, email_on, sms_on, ads_on in settings_data]


# Error Handling

    except sqlite3.Error as err:
        print("There was an error while loading settings from the database: ", err)


# Closure

    finally:
        if connection:
            connection.commit()
            connection.close()


                           #-------------------------#
#--------------------------#    Save All Settings    #-------------------------#
                           #-------------------------#

        # Saves all settings of all users from config.Settings to database #

def save_all_settings():


# Connect to Database

    connection, cursor = connect_to(DBSettings)

    if connection is None:
        return


# Query Definition

    query = '''
        INSERT INTO settings (
            username,
            language,
            email_on,
            sms_on,
            ads_on
        )
        VALUES (?, ?, ?, ?, ?);
    '''

# Out with the old, in with the new

    try:
        cursor.execute("DELETE FROM settings;")

        for each_user in config.Settings:
            cursor.execute(query,
                (
                    each_user['Username'],
                    each_user['Language'],
                    each_user['Email On'],
                    each_user['SMS On'],
                    each_user['Ads On']
                )
            )


# Error Handling

    except sqlite3.Error as err:
        print("There was an error uploading settings to the database: ", err)


# Closure

    finally:

        if connection:
            connection.commit()
            connection.close()



                            #----------------------#
#---------------------------#    Toggle Setting    #---------------------------#
                            #----------------------#

               # Allows the user to toggle their settings on/off #

def toggle_setting(on):

    if config.UserSettings[on]: config.UserSettings[on] = False
    else: config.UserSettings[on] = True

    save_user_settings()



                            #-----------------------#
#---------------------------#    Change Language    #--------------------------#
                            #-----------------------#

           # Allows the user to change the language for their account #

def change_language(language):

    if language == 'English':
        config.UserSettings['Language'] = 'Spanish'

    else: config.UserSettings['Language'] = 'English'

    save_user_settings()



#----------------------------#----------------------#--------------------------#
#----------------------------#    Guest Controls    #--------------------------#
#----------------------------#----------------------#--------------------------#

                              # The Settings Menu #

def guest_controls():


# Menu

    while True:

        print("")
        print("|----------------------------|")
        print("           Settings           ")
        print("|----------------------------|")
        print("")


# Options

        if config.UserSettings['Email On']:
            print("   [1] Email : On")
        else:
            print("   [1] Email : Off")

        if config.UserSettings['SMS On']:
            print("    [2] SMS : On")
        else:
            print("    [2] SMS : Off")

        if config.UserSettings['Ads On']:
            print("     [3] Targeted Ads : On")
        else:
            print("     [3] Targeted Ads : Off")

        print("")
        print("                                         Return [>] ")


# Prompt

        control_choice = input("Please select an option (or press Enter to return): ")


# Outcomes

        if control_choice == "1":
            toggle_setting('Email On')

        elif control_choice == "2":
            toggle_setting('SMS On')

        elif control_choice == "3":
            toggle_setting('Ads On')

        elif control_choice == ">": return True
        elif control_choice == "": return False


# Error Handling

        else:
            print("Invalid input. Please enter an available option.")


# End of File
