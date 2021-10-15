"""
# 
# File          : q3.py
# Created       : 15/10/21 10:16 AM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""

course_list = {}


def add_course():
    # function to add new course name and course code

    course_name = input("Enter the Course name\n")
    course_code = input("Enter the course code\n")
    course_list[course_code] = course_name


def edit_course():
    # function to edit course name

    c_code = input("Please enter the course code you want to edit: {}\n". format(course_list))
    if c_code in course_list:
        old_name = course_list[c_code]
        new_name = input("Enter the course name\n")
        course_list[c_code] = new_name
        print("Course name changed successfully\n {} -> {}".format(old_name, new_name))
    else:
        print("Please enter a valid code")


if __name__ == '__main__':
    # main function to read user option

    while 1:
        user_option = int(input("1. Add Course code and course name\n2. Edit Course Name\n3. Print Data\n4. Exit\n"))
        if user_option == 1:
            add_course()
        elif user_option == 2:
            edit_course()
        elif user_option == 4:
            break
