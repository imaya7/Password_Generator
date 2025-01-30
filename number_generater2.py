import os
import random
import string
import datetime

class PasswordGenerator:
    def __init__(self, words_file):
        """
        starts the password generator with the list of words loaded from the given file.
        """
        # finds file path for the words file
        words_file_path = os.path.join(os.path.dirname(__file__), words_file)
        try:
            with open(words_file_path, 'r') as file:
                # Load the words into a list, removing any extra whitespace
                self.words = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"Error: The file '{words_file}' could not be found.")
            raise

    def generate_memorable_password(self, num_words, case_style):
        """
        Creates a memorable password by picking a few random words + a random digit to each.
        The cases can be changed according to the chosen style ( all lowercase, uppercase or both).
        """
        selected_words = random.sample(self.words, num_words)
        password_parts = []

        for word in selected_words:
            # Changes case according to the chosen style
            if case_style == 'lower':
                word = word.lower()
            elif case_style == 'upper':
                word = word.upper()
            elif case_style == 'capitalize':
                word = word.capitalize()
            elif case_style == 'both':
                word = ''.join(random.choice([c.lower(), c.upper()]) for c in word)

            # adds a random number (0-9) to each word for better security measures
            number = random.randint(0, 9)
            password_parts.append(f"{word}{number}")

        # Join all the parts with a hyphen + return the result
        return '-'.join(password_parts)

    def generate_random_password(self, length, include_punctuation, exclude_chars):
        """
        (same thing but for random) 
        creates a random password by choosing characters which are from a collection of letters, digits, and optionally punctuation.
        Also makes sure to excluded characters (if any) are filtered out from the collection. 
        """
        # Start with letters and digits, and optionally include punctuation
        char_pool = string.ascii_letters + string.digits
        if include_punctuation:
            char_pool += string.punctuation

        # Remove any excluded characters from the collection
        char_pool = ''.join([c for c in char_pool if c not in exclude_chars])

        # Create a password by randomly picking characters from the collection
        password = ''.join(random.choice(char_pool) for _ in range(length))
        return password

    def save_password(self, password, password_type):
        """
        Saves the generated password to a file in a folder named after the password type, labled with the type it is Memorable or Random
        Each password has a timestamp next to it of when it was generated.
        """
        # Create a directory for the password type (if it doesn't exist)
        dir_path = os.path.join(os.path.dirname(__file__), password_type.capitalize())
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Log the password to a text file with the current date and time
        file_path = os.path.join(dir_path, "Generated_Passwords.txt")
        current_time = datetime.datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p")
        with open(file_path, 'a') as file:
            file.write(f"{password} - Generated on: {current_time}\n")

    def generate_1000_passwords(self, password_type):
        """
        creates and saves 1000 passwords based on the chosen type either memorable or random
        """
        for _ in range(1000):
            if password_type == 'memorable':
                num_words = random.randint(3, 5)
                case_style = random.choice(['lower', 'upper', 'capitalize', 'both'])
                password = self.generate_memorable_password(num_words, case_style)
            else:
                length = random.randint(8, 16)
                include_punctuation = random.choice([True, False])
                exclude_chars = random.choice([[], ['a', 'A']])
                password = self.generate_random_password(length, include_punctuation, exclude_chars)
            
            # Save the generated password to the appropriate file
            self.save_password(password, password_type)

# Example usage
if __name__ == "__main__":
    # Specify the path for the words file
    words_file = os.path.join(os.path.dirname(__file__), 'top_english_nouns_lower_100000.txt')
    try:
        generator = PasswordGenerator(words_file)
    except Exception as e:
        print(e)
        exit()

    # Ask the user if they want to generate passwords
    user_choice = input("Do you want to generate 1000 password combinations? (Enter 'yes' or 'no'): ").strip().lower()

    if user_choice == 'yes':
        # Randomly choose between generating memorable or random passwords
        password_type = random.choice(['memorable', 'random'])
        generator.generate_1000_passwords(password_type)
        print(f"1000 {password_type} passwords have been generated and saved.")
    elif user_choice == 'no':
        print("No passwords were generated.")
    else:
        print("Oops! That wasn't a valid answer. Please enter 'yes' or 'no'.")
