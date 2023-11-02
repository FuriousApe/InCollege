
                            #########################
#################################               ################################
#################################  S K I L L S  ################################
#################################               ################################
                            #########################

                    # All code pertaining to skill-learning. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import config

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Learn Skill Functions                      #
#                             [ 2 ] Skill Menu                                 #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                          #---------------------------#
#-------------------------#   Learn Skill functions   #------------------------#
                          #---------------------------#

def time_management():
    config.under_construction()

def communication():
    config.under_construction()

def networking():
    config.under_construction()

def team_building():
    config.under_construction()

def organization():
    config.under_construction()


#------------------------------#------------------#----------------------------#
#------------------------------#    Skill Menu    #----------------------------#
#------------------------------#------------------#----------------------------#

def menu():


    skills = [
                "Time Management",
                "Communication",
                "Networking",
                "Team Building",
                "Organization"
             ]


# Skill Enumeration

    while True:

        print("\nSelect a skill you'd like to learn: ")

        for i, skill in enumerate(skills, start = 1):
            print(f"{i}. {skill}")

        print("0. Return to the Main Menu")

        choice = input("Please select an option (or press Enter to return): ")


# Skill Selection

        if choice == "0" or choice == "": return
        elif choice == "1": time_management()
        elif choice == "2": communication()
        elif choice == "3": networking()
        elif choice == "4": team_building()
        elif choice == "5": organization()

        else:
            print("Invalid input. Please enter an available option.")



# End of File
