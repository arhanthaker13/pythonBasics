# Arhan Thaker, aat77@uakron.edu
# Programming for Data Science
# Copyright @2024, Arhan Thaker, All rights reserved.
# Data Science Assgn 1
# This program prompts the user to input a single uppercase letter converts 
# it to its ASCII value, and then transforms the letter to lowercase

def main():  
    while True:
        user_letter = (input("Enter a letter between A and capital Z: "))
        print()

        # validate user input (string lenght = 1 and Capital Letter)
        if(len(user_letter) > 1 or 'A' > user_letter or user_letter > 'Z'):
            print("Invalid Input! Try again.")
        else:
            break

    # convert user input to ascii
    upper_ascii = ord(user_letter)
    print(f"The letter {user_letter} in ascii is {upper_ascii}.\n")

    # convert capital letter to lower case by adding 32
    lower_letter = chr(upper_ascii + 32)
    print("Converting to lower case...")
    print(f"User input in lowercase is {lower_letter}")
    print()

main()
