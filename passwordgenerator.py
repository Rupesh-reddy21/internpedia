import string
import secrets
def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if not characters:
        print("Error: At least one character set must be selected.")
        return None
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Secure Password Generator!")
    while True:
        try:
            length = int(input("\nEnter password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'
    password = generate_password(length, uppercase, lowercase, digits, symbols)
    if password:
        print("\nGenerated Password:", password)
        copy_to_clipboard = input("Do you want to copy the password to clipboard? (y/n): ").lower()
        if copy_to_clipboard == 'y':
            pyperclip.copy(password)
            print("Password copied to clipboard.")
    again = input("\nDo you want to generate another password? (y/n): ").lower()
    if again == 'y':
        main()
    else:
        print("Thank you for using Secure Password Generator!")
if __name__ == "__main__":
    main()