import random
import string
from word2number import w2n
def generate_password():
    print("__Welcome to the Password Generator__")
    while True:
        try:
            length = (input("Enter the desired length of the password: "))
            if length.isdigit():
                length = int(length)
            else:
                length = w2n.word_to_num(length)
            if length <= 0:
                print("Length must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    characters = string.ascii_letters + string.digits + string.punctuation
    try:
        password = "".join(random.choice(characters) for i in range(length))
        print("__Generating Password__")
        print(f"Your generated password is: {password}")
    except IndexError:
        print("An error occurred while generating the password. Please try again.")
if __name__ == "__main__":
    generate_password()


