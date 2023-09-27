
                          #############################
###############################                   ##############################
###############################  P O L I C I E S  ##############################
###############################                   ##############################
                          #############################

                # One page for all of our policies and notices. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import config
import settings_

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Privacy Policy                             #
#                                                                              #
#                             [ 2 ] Copyright Notice                           #
#                             [ 3 ] About                                      #
#                             [ 4 ] Accessibility                              #
#                             [ 5 ] User Agreement                             #
#                             [ 6 ] Cookie Policy                              #
#                             [ 7 ] Copyright Policy                           #
#                             [ 8 ] Brand Policy                               #
#                                                                              #
#                             [ 9 ] Languages                                  #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                            #----------------------#
#---------------------------#    Privacy Policy    #---------------------------#
                            #----------------------#

           # Informs user of Privacy Policy; links to Guest Controls #

def privacy():

    while True:


# Is User Signed In?

        if config.User is None: signed_in = False
        else: signed_in = True


# Menu Display

        print("__________________")
        print("  Privacy Policy |____________________________________")

        print("\n   We only use your personal information for the")
        print("     purpose of improving the InCollege app and/or")
        print("     any other venture in the future of Team Colorado")
        print("     and any of our associates henceforth.\n")

        print("\n   While on the InCollege app, we collect the")
        print("     information sent by your browser or device. This")
        print("     may include details such as your IP address, page")
        print("     history (within our application or site) or amount")
        print("     of time spent within the app itself.\n")


# Option Available if Signed In

        if signed_in:
            print(" [<] Guest Controls                       Go Back [>] ")
        else:
            print("                                          Go Back [>] ")


# Prompt
        stay_in_menu = True
        privacy_choice = input("Please select an option (or press Enter to return): ")


# Outcomes

        if privacy_choice == '': return False
        elif privacy_choice == '>': return True
        elif privacy_choice == '<': stay_in_menu = settings_.guest_controls()


# Error Handling

        else:
            print("Invalid input. Please enter an available option.")


# Option from Guest Controls

        if stay_in_menu: continue
        else: return False


                           #------------------------#
#--------------------------#    Copyright Notice    #--------------------------#
                           #------------------------#

def notice():

    while True:

        print("______________________")
        print("  A Copyright Notice |________________________________")

        print("\n   (C) 2023 Team Colorado. All rights reserved.")
        print("     InCollege, the InCollege Logo and InCollege apps")
        print("     are trademarks of Team Colorado Inc.\n")

        print("                                          Go Back [>] ")


        copyright_choice = input("Please select an option (or press Enter to return): ")

        if copyright_choice == '': return False
        elif copyright_choice == '>': return True

        else:
            print("Invalid input. Please enter an available option.")


                                 #-------------#
#--------------------------------#    About    #-------------------------------#
                                 #-------------#

def about():

    print("_________")
    print("  About |_____________________________________________")

    print("\n   InCollege is the largest college student network")
    print("     in the world. Our mission and purpose is to help")
    print("     newcomers to the professional workplace as they")
    print("     prepare to begin their careers.\n")

    print("\n   We help students find jobs without the stress of")
    print("     competing against seasoned professionals. If a")
    print("     student needs help getting connected, they can")
    print("     come to InCollege, where we level the playing field.\n")

    print("                                          Go Back [>] ")

    about_choice = input("Please select an option (or press Enter to return): ")

    if about_choice == '': return False
    elif about_choice == '>': return True

    else:
        print("Invalid input. Please enter an available option.")


                            #---------------------#
#---------------------------#    Accessibility    #----------------------------#
                            #---------------------#

def accessibility():

    print("_________________")
    print("  Accessibility |_____________________________________")

    print("\n   InCollege, and the Team Colorado group, are")
    print("     dedicated to providing accessible content and")
    print("     services.\n")

    print("\n   Contact us at support@InCollege.com if you have")
    print("     questions, comments, or concerns.")
    print("                                          Go Back [>] ")

    access_choice = input("Please select an option (or press Enter to return): ")

    if access_choice == '': return False
    elif access_choice == '>': return True

    else:
        print("Invalid input. Please enter an available option.")


                            #----------------------#
#---------------------------#    User Agreement    #---------------------------#
                            #----------------------#

def user_agreement():

    print("__________________")
    print("  User Agreement |____________________________________")

    print("\n   InCollege and its affiliates are responsible")
    print("     for maintaining confidentiality and discretion")
    print("     when collecting personal information from")
    print("     from its users.\n")

    print("\n   By using the InCollege app and accepting its")
    print("     services, you hereby agree to comply with our")
    print("     policies and all applicable rules and regulations.\n")

    print("                                          Go Back [>] ")

    agreement_choice = input("Please select an option (or press Enter to return): ")

    if agreement_choice == '': return False
    elif agreement_choice == '>': return True

    else:
        print("Invalid input. Please enter an available option.")


                                #---------------#
#-------------------------------#    Cookies    #------------------------------#
                                #---------------#

def cookies():

    print("_________________")
    print("  Cookie Policy |_____________________________________")

    print("\n   InCollege may, at any point in time, resort to")
    print("     the use of cookies or other forms of digital")
    print("     tracking when you use our app or visit our site.\n")

    print("\n   The use of the aforementioned tracking is to")
    print("     improve our user experience and better our services.\n")

    print("\n   We reserve the right to alter this policy at any")
    print("     given time or for any given reason. We agree to")
    print("     notify you of any changes made via this page.\n")

    print("                                          Go Back [>] ")

    cookie_choice = input("Please select an option (or press Enter to return): ")

    if cookie_choice == '': return False
    elif cookie_choice == '>': return True

    else:
        print("Invalid input. Please enter an available option.")


                               #-----------------#
#------------------------------#    Copyright    #-----------------------------#
                               #-----------------#

def copy_right():

    print("____________________")
    print("  Copyright Policy |__________________________________")

    print("\n   At InCollege, as well as the entire Team Colorado")
    print("     group and all its affiliates, present and future,")
    print("     respect the rights of others, including those that")
    print("     pertain to intellectual property.\n")

    print("\n   This application obeys the standards laid out by")
    print("     the Digital Millennium Copyright Act of 1998.\n")

    print("\n   We also expect any and all users to conduct")
    print("     themselves in the same manner. Infringing on the")
    print("     rights of others will result in the immediate")
    print("     termination of said user's account and the")
    print("     notification of a DMCA Registered Agent.\n")

    print("                                          Go Back [>] ")

    copyright_choice = input("Please select an option (or press Enter to return): ")

    if copyright_choice == '': return False
    elif copyright_choice == '>': return True

    else:
        print("Invalid input. Please enter an available option.")


                                 #-------------#
#--------------------------------#    Brand    #-------------------------------#
                                 #-------------#

def brand():

    print("________________")
    print("  Brand Policy |______________________________________")

    print("\n   It is the policy of the entire InCollege team")
    print("     to help ensure the betterment of college students")
    print("     across the globe, as well as the solidification")
    print("     of their professional future.\n")

    print("\n   By helping students to connect with one another,")
    print("     and with professional peers, we hope to see a")
    print("     far greater number of recent college graduates")
    print("     secure the life that they, and their loved ones,")
    print("     hope they might one day achieve.\n")

    print("                                          Go Back [>] ")

    brand_choice = input("Please select an option (or press Enter to return): ")

    if brand_choice == '': return False
    elif brand_choice == '>': return True

    else:
        print("Invalid input. Please enter an available option.")

                               #-----------------#
#------------------------------#    Languages    #-----------------------------#
                               #-----------------#
def languages():

    while True:


# Menu Display

        print("_____________")
        print("  Languages |_________________________________________")

        print("      [1] Language :", config.UserSettings['Language'])
        print("                                         Return [>] ")


# Prompt

        lang_choice = input("Please select an option (or press Enter to return): ")


# Outcomes

        if lang_choice == '': return False
        elif lang_choice == '>': return True
        elif lang_choice == '1': settings_.change_language(config.UserSettings['Language'])


# Error Handling

        else:
            print("Invalid input. Please enter an available option.")


# End of File