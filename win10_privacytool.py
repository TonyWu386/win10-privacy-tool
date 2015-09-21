# -----------------------------------------------------------------------------
# File name: win10_privacytool.py                                             #
# Date created: 8/1/2015                                                      #
# Date last modified: 8/3/2015                                                #
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
    
    print ("Make sure to run as admin.")
    print ("Warning! This program modifies the Windows hosts file!")
    command = input("Do you want to proceed? (yes/no)")
    
    if command == "yes":

        hostslist = open('hostslist.txt', 'r')

        hostsfile = open('C:\Windows\System32\Drivers\etc\hosts', 'a')

        for line in hostslist:
            hostsfile.write(line)

        print ("Operation complete.")

    else:

        print ("Operation aborted. The hosts file has not been modified.")
