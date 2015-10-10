# -----------------------------------------------------------------------------
# File name: win10_privacytool.py                                             #
# Date created: 8/1/2015                                                      #
# Date last modified: 10/10/2015                                              #
#                                                                             #
# Author: Tony Wu (Xiangbo)                                                   #
# Email: xb.wu@mail.utoronto.ca                                               #
#                                                                             #
# Python version: 3.4                                                         #
# Dependencies: None                                                          #
#                                                                             #
# License: GNU GPL v2.0                                                       #
#                                                                             #
# Copyright (c) 2014-2015 [Tony Wu], All Right Reserved                       #
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    DEFAULT_LOCATION = "C:\Windows\System32\Drivers\etc\hosts"
    ERROR_MSG = "Invalid input! Aborting..."

    print ("Make sure to run as admin.")
    print ("Warning! This program modifies the Windows hosts file!")
    command = input("Do you want to proceed? (yes/no)")

    if command == "yes":

        command = input("Using default directory? (yes/no)")

        if command in ["yes", "no"]:

            if command == "no":
                print("The default location is " + DEFAULT_LOCATION)
                hostPath = input("Enter custom location of hosts file:")
            else:
                print("Setting location to " + DEFAULT_LOCATION)
                hostPath = DEFAULT_LOCATION

            hostsList = open('hostslist.txt', 'r')
            hostsFile = open(hostPath, 'r')

            listLines = hostsList.readlines()
            fileLines = hostsFile.readlines()

            hostsList.close()
            hostsFile.close()
            command = input("Add or remove blocking entries? (add/rem)")

            if command == "add":
                newLines = fileLines[:]
                for line in listLines:
                    newLines.append(line)
            elif command == "rem":
                newLines = [x for x in fileLines if x not in listLines]
            else:
                print(ERROR_MSG)

            if command in ["add", "rem"]:

                hostsFile = open(hostPath, 'w')

                for line in newLines:
                    hostsFile.write(line)

                hostsFile.close()
                print ("Operation complete.")
        else:
            print(ERROR_MSG)
    elif command == "no":
        print("Aborting...")
    else:
        print (ERROR_MSG)
