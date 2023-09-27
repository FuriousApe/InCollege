
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
#           ['Username': ],
#           ['Password': ],
#           ['First Name': ],
#           ['Last Name': ]

UserSettings = None
# Dictionary
# Holds the user's chosen settings after login
#
#           ['Username': ],
#           ['Language': English],
#           ['Email On': True],
#           ['SMS On': True],
#           ['Ads On': True]


Accounts = None
# Dictionaries
# Holds all users' personal info after load_accounts()

Settings = None
# Dictionaries
# Holds each users' chosen settings after load_settings()

Jobs = None
# Dictionaries
# Holds all posted jobs after load_jobs()


Connection = None
# Occasionally used to hold active DB connection for error avoidance


# Passwords
PasswordMinLength = 8
PasswordMaxLength = 12

# Limitations
MaxAccounts = 5
MaxJobs = 5


                               #------------------#
#------------------------------#    File Paths    #----------------------------#
                               #------------------#

# Databases
DBAccounts = 'student_accounts.db'
DBSettings = 'user_settings.db'
DBJobs = 'job_postings.db'


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
