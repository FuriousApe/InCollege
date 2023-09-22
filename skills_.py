
                            #########################
#################################               ################################
#################################  S K I L L S  ################################
#################################               ################################
                            #########################

                    # All code pertaining to skill-learning. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#




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

    print("")
    print("  / / / / / / / / / / / / / / / / / / / /")
    print(" / / / / /  UNDER CONSTRUCTION / / / / /")
    print("/ / / / / / / / / / / / / / / / / / / /")
    print("")


def communication():

    print("")
    print("  / / / / / / / / / / / / / / / / / / / /")
    print(" / / / / /  UNDER CONSTRUCTION / / / / /")
    print("/ / / / / / / / / / / / / / / / / / / /")
    print("")


def networking():

    print("")
    print("  / / / / / / / / / / / / / / / / / / / /")
    print(" / / / / /  UNDER CONSTRUCTION / / / / /")
    print("/ / / / / / / / / / / / / / / / / / / /")
    print("")


def team_building():

    print("")
    print("  / / / / / / / / / / / / / / / / / / / /")
    print(" / / / / /  UNDER CONSTRUCTION / / / / /")
    print("/ / / / / / / / / / / / / / / / / / / /")
    print("")


def organization():

    print("")
    print("  / / / / / / / / / / / / / / / / / / / /")
    print(" / / / / /  UNDER CONSTRUCTION / / / / /")
    print("/ / / / / / / / / / / / / / / / / / / /")
    print("")



#------------------------------#------------------#----------------------------#
#------------------------------#    Skill Menu    #----------------------------#
#------------------------------#------------------#----------------------------#

def skill_menu():


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

        choice = input("Select a number 0-5: ")


# Skill Selection

        if choice == "0":
            return

        elif choice == "1": time_management()

        elif choice == "2": communication()

        elif choice == "3": networking()

        elif choice == "4": team_building()

        elif choice == "5": organization()

        else:
            print("Your input is invalid. Please select a number 0-5.")



# End of File
