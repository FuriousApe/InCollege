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

user = None
# Object
# Represents the current user after login


profile = None
# Object
# Represents the current user's profile after login


settings = None
# Object
# Represents the current user's settings after login


# Passwords
PasswordMinLength = 8
PasswordMaxLength = 12

# Limitations
MaxAccounts = 10
MaxJobs = 10


                               #------------------#
#------------------------------#    File Paths    #----------------------------#
                               #------------------#

# Databases
DB = 'incollege_database.db'


                               #-----------------#
#------------------------------#    Functions    #-----------------------------#
                               #-----------------#

# Under Construction
def under_construction():
    print("")
    print("  / / / / / / / / / / / / / / / / / / / /")
    print(" / / / / /  UNDER CONSTRUCTION / / / / /")
    print("/ / / / / / / / / / / / / / / / / / / /")
    print("")



def capitalize_each_word(input_str):
    return ' '.join([word.capitalize() for word in input_str.split()])




# End of File
