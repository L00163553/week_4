"""
# File          : q3.py
# Created       : 15/10/21 10:16 AM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
import pprint

COURSE_LIST = {}


def add_course():
    """function to add new course name and course code"""

    course_name = input("Enter the Course name\n")
    course_code = input("Enter the course code\n")
    COURSE_LIST[course_code] = course_name


def edit_course():
    """function to edit course name"""

    c_code = input("Please enter the course code you want to edit: {}\n".format(COURSE_LIST))
    if c_code in COURSE_LIST:
        old_name = COURSE_LIST[c_code]
        new_name = input("Enter the course name to update\n")
        COURSE_LIST[c_code] = new_name
        print("Course name changed successfully\n {} -> {}\n".format(old_name, new_name))
    else:
        print("Please enter a valid code")


def display_data():
    """function to display course list"""

    pretty_print = pprint.PrettyPrinter(indent=4)
    pretty_print.pprint(COURSE_LIST)


if __name__ == '__main__':
    """main function to read user option"""

    while 1:
        USER_OPTION = int(input("1. Add Course code and course name\n"
                                "2. Edit Course Name\n3. Print Data\n4. Exit\n"))
        if USER_OPTION == 1:
            add_course()
        elif USER_OPTION == 2:
            edit_course()
        elif USER_OPTION == 3:
            display_data()
        elif USER_OPTION == 4:
            break
        else:
            print("Please enter a valid option")
