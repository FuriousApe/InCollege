
                     #######################################
##########################                             #########################
##########################  T E A M   C O L O R A D O  #########################
##########################                             #########################
                     #######################################

                             #--------------------#
#----------------------------#    Dependencies    #----------------------------#
                             #--------------------#

from data_ import create_student_table, create_job_table
from accounts_ import login_menu





                                #################
###################################  M A I N  ##################################
                                #################

                 # Creates tables if they don't already exist #
                     # Directs user to the login screen #

if __name__ == "__main__":

    create_student_table()
    create_job_table()
    login_menu()


# End of File
