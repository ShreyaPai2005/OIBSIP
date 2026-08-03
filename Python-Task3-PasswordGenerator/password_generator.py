import random
import string

while True:

    length = int(input("Enter the password length (minimum 8): "))

    if length < 8:
        print("Password length must be at least 8 characters.")
        continue

    use_upper = input("Include uppercase letters? (yes/no): ")
    use_lower = input("Include lowercase letters? (yes/no): ")
    use_numbers = input("Include numbers? (yes/no): ")
    use_symbols = input("Include special characters? (yes/no): ")

    characters = ""

    if use_upper.lower() == "yes":
        characters += string.ascii_uppercase

    if use_lower.lower() == "yes":
        characters += string.ascii_lowercase

    if use_numbers.lower() == "yes":
        characters += string.digits

    if use_symbols.lower() == "yes":
        characters += string.punctuation

    if characters == "":
        print("You must select at least one character type.")
        continue

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    again = input("\nGenerate another password? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the Password Generator!")
        break