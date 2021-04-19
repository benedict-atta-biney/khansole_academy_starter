"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example


# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
Initial_number = 0

while Initial_number < 3:
    Number_1 = random.randint(10, 99)
    Number_2 = random.randint(10, 99)
    Sum_Number_is_answer = Number_1 + Number_2

    user_answer = input('What is the answer for ' + str(Number_1) + ' + ' + str(Number_2) + '?:')
    if int(user_answer) == Sum_Number_is_answer:
        Initial_number += 1
        print("Wow! You are correct {} in a row".format(Initial_number))
    else:
        print("Incorrect answer. The expected answer is :  {}".format(Sum_Number_is_answer))

        Initial_number = 0
print("Congratulations! You have mastered addition")
