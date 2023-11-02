
                          #############################
###############################                   ##############################
###############################  S E T T I N G S  ##############################
###############################                   ##############################
                          #############################

                     # All code the pertains to user settings. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import config
from data_ import connect_to_database



#----------------------------#----------------------#--------------------------#
#----------------------------#    Guest Controls    #--------------------------#
#----------------------------#----------------------#--------------------------#

                              # The Settings Menu #

def guest_controls():


    # Menu
    while True:

        user = config.user
        settings = config.settings

        print("")
        print("|----------------------------|")
        print("           Settings           ")
        print("|----------------------------|")
        print("")

        # Options
        if settings.email_on:
            print("   [1] Email : On")
        else:
            print("   [1] Email : Off")

        if settings.sms_on:
            print("    [2] SMS : On")
        else:
            print("    [2] SMS : Off")

        if settings.ads_on:
            print("     [3] Targeted Ads : On")
        else:
            print("     [3] Targeted Ads : Off")

        print("")
        print("                                         Return [>] ")

        # Prompt
        choice = input("Please select an option (or press Enter to return): ")

        # Outcomes
        if choice == "1": settings.email_on = user.toggle_setting('email_on')
        elif choice == "2": settings.sms_on = user.toggle_setting('sms_on')
        elif choice == "3": settings.ads_on = user.toggle_setting('Ads_on')

        elif choice == ">": return True
        elif choice == "": return False

        # Error Handling
        else: print("Invalid input. Please enter an available option.")




# End of File
