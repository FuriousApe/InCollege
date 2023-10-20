
                      #######################################
###########################                             ########################
###########################  C O N F I G U R A T I O N  ########################
###########################                             ########################
                      #######################################

                  # The one-stop shop for app configuration. #

          # Changes here will be reflected throughout the program. #

                               #-----------------#
#------------------------------#    Variables    #-----------------------------#
                               #-----------------#

User = None
# Dictionary
# Holds the user's personal info after login
#
#       CURRENT KEYS:       'Username' : String
#                           'Password' : String
#                           'First Name' : String
#                           'Last Name' : String
#                           'University' : String
#                           'Major' : String
#                           'Created a Profile' : Bool


UserProfile = None
# Dictionary
# Holds the user's profile info after login
#
#       CURRENT KEYS:       'Username' : String
#                           'Title' : String
#                           'About Me' : String
#                           'University' : String
#                           'Major' : String
#                           'Years Attended' : String
#                           'Job 1 : Title' : String
#                           'Job 1 : Employer' : String
#                           'Job 1 : Date Started' : String
#                           'Job 1 : Date Ended' : String
#                           'Job 1 : Location' : String
#                           'Job 1 : Description' : String
#                           ...
#                           'Job 3 : Description' : String



UserSettings = None
# Dictionary
# Holds the user's chosen settings after login
#
#       CURRENT KEYS:       'Username' : String
#                           'Language' : String
#                           'Email On' : Bool
#                           'SMS On' : Bool
#                           'Ads On' : Bool


Accounts = None
# Dictionaries
# Holds all users' personal info after load_accounts()

Profiles = None
# Dictionaries
# Holds all users' profile info after load_profiles()

Settings = None
# Dictionaries
# Holds each users' chosen settings after load_settings()

Jobs = None
# Dictionaries
# Holds all posted jobs after load_jobs()

Requests = None
# Dictionaries
# Holds all requests after load_requests()

Connections = None
# Dictionaries
# Holds all connections after load_connections()

Connection = None
# Occasionally used to hold active DB connection for error avoidance


# Passwords
PasswordMinLength = 8
PasswordMaxLength = 12

# Limitations
MaxAccounts = 10
MaxJobs = 5


                               #------------------#
#------------------------------#    File Paths    #----------------------------#
                               #------------------#

# Databases
DBAccounts = 'student_accounts.db'
DBProfiles = 'user_profiles.db'
DBSettings = 'user_settings.db'
DBJobs = 'job_postings.db'
DBRequests = 'requests.db'
DBConnections = 'connections.db'


                                 #--------------#
#--------------------------------#    Labels    #------------------------------#
                                 #--------------#

# Under Construction
def under_construction():
    print("")
    print("  / / / / / / / / / / / / / / / / / / / /")
    print(" / / / / /  UNDER CONSTRUCTION / / / / /")
    print("/ / / / / / / / / / / / / / / / / / / /")
    print("")



# End of File
