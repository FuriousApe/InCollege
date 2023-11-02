
                       ###################################
############################                         ###########################
###########################  A P P L I C A T I O N S  ##########################
############################                         ###########################
                       ###################################

                  # All code pertaining to job applications. #

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

import sqlite3
import re

                           #-------------------------#
#--------------------------#    Table of Contents    #-------------------------#
#                          #-------------------------#                         #
#                                                                              #
#                             [ 1 ] Input Validation                           #
#                             [ 2 ] Apply for Job                              #
#                                                                              #
#------------------------------------------------------------------------------#


                           ###########################
##############################  F U N C T I O N S  #############################
                           ###########################

                           #------------------------#
#--------------------------#    Input Validation    #--------------------------#
                           #------------------------#

def get_date_input(prompt):

    while True:
        date_str = input(prompt)
        if re.match("^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\\d{4}$", date_str):
            month, day, year = date_str.split('/')
            return f"{year}-{month}-{day}"
        print("Invalid date format. Please use mm/dd/yyyy.")

def get_app_text_input(prompt):

    while True:
        app_text = input(prompt)
        if len(app_text) >= 10:
            return app_text
        print("Your explanation is too short. Please provide more details.")



                             #---------------------#
#----------------------------#    Apply for Job    #---------------------------#
                             #---------------------#

def apply_for_job(username, job):

    if username == job.username:
        print("You can't apply to your own job. That's called self-employment... and you don't need our services for that.")
        return

    sql_grad_date = get_date_input("Enter your graduation date (mm/dd/yyyy): ")
    sql_start_date = get_date_input("Enter the date you can start working (mm/dd/yyyy): ")
    app_text = get_app_text_input("Explain why you think you would be a good fit for this job: ")

    job.apply(username, sql_grad_date, sql_start_date, app_text)

    print("Application completed!")







# End of file
