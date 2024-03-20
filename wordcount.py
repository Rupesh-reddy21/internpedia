import string
def count_words(text):
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.split()
    word_count = len(words)
    return word_count
def get_text_from_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("Error: File not found.")
        return None
def main():
    print("Welcome to Word Counter!")
    while True:
        choice = input("\nEnter '1' to input text manually or '2' to input text from a file: ")
        if choice == '1':
            text = input("Enter the text: ")
            break
        elif choice == '2':
            filename = input("Enter the filename: ")
            text = get_text_from_file(filename)
            if text:
                break
        else:
            print("Invalid choice. Please enter '1' or '2'.")
    if text:
        word_count = count_words(text)
        print(f"\nThe number of words in the text: {word_count}")
    again = input("\nDo you want to count words for another text? (yes/no): ").lower()
    if again == 'yes':
        main()
    else:
        print("Thank you for using Word Counter!")
if __name__ == "__main__":
    main()