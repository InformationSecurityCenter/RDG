#! /usr/bin/python3

import sys
import os


def ON_state():
    site_ID = sys.argv[1]
    command1 = ""
    if (site_ID == "1"):
        command1 = "sudo a2ensite site1.conf"

    if (site_ID == "2"):
        command1 = "sudo a2ensite site2.conf"

    if (site_ID == "3"):
        command1 = "sudo a2ensite site3.conf"

    command2 = "sudo service apache2 reload"

    os.system(command1)
    os.system(command2)


def OFF_state():
    site_ID = sys.argv[1]
    command1 = ""
    if (site_ID == "1"):
        command1 = "sudo a2dissite site1.conf"

    if (site_ID == "2"):
        command1 = "sudo a2dissite site2.conf"

    if (site_ID == "3"):
        command1 = "sudo a2dissite site3.conf"

    command2 = "sudo service apache2 reload"

    os.system(command1)
    os.system(command2)

if sys.argv[2] == "ON":
    ON_state()
else:
    OFF_state()

