"""
# 
# File          : q2.py
# Created       : 11/10/21 3:13 PM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   : Python  script  to  encrypt  a  password and calculate the time taken to encrypt the password
#
"""

import timeit
from cryptography.fernet import Fernet


def encrypt_password(password):
    # Function to encrypt the password
    # key to encrypt the password
    key = b'PCHl_MjGyEyBxLYha3S-cWg_SDDmjT4YYaKYh4Z7Yug='
    cipher_suite = Fernet(key)
    encrypted_pwd = cipher_suite.encrypt(password)
    # return the encrypted password
    return encrypted_pwd


if __name__ == '__main__':
    # Main Method

    pwd = input("Please enter the password to encrypt: ")
    start_time = timeit.default_timer()
    print("The start time is :", start_time)
    encrypted_pwd = encrypt_password(pwd.encode())
    # Calculate the time taken to encrypt the password
    print("Time taken to encrypt {:.4f}".format(timeit.default_timer() - start_time))
    print("Encrypted Password: {}".format(encrypted_pwd))
