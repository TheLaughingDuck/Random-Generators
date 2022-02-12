# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 15:53:03 2022

@author: jorst
"""

#PACKAGES
from random import choices


#SETUP
characters = "abcdefghijklmnopqrstuvwxyzåäö-.,!#\"¤%&()[]{}+^*:;<>"
char_list = list(characters)


#PASSWORD CREATION
def create_password(length, words):
    
    for i in range(0, words):
        pword = choices(char_list, k=length)
        pword = ''.join(pword)
        
        print(pword)


#USER INTERFACE
print("Please select desired password length. A strong password has 16 or more characters")
leng = int(input(">>"))
print("----------")

active_program = True

while active_program != "stop":
    create_password(leng, 20)
    
    print("----------")
    print("Please randomly select one of the passwords above.")
    print("Write \"stop\" to end the program. Write anything else to generate new passwords")
    active_program = input(">>")


#CLEAR VARIABLES
del leng




