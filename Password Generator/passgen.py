# This Python script generates a random password of a specified length by using a combination of letters, digits, and punctuation marks.
import random
import string

def generate_password(int_length):    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(int_length))
    return password

while True:
    length = input("Enter the length of the password (or press 'Q' to quit) : ")
    if length.lower() == 'q':
        break 
    try:
        final_length = int(length)
        password = generate_password(final_length)
        print(f"Generated password : {password}")
    except ValueError:
        print("Please enter a valid integer for the password length.")