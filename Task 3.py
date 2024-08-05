import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_sets = {
        'letters': string.ascii_letters,
        'numbers': string.digits,
        'symbols': string.punctuation
    }
    
    characters = ''
    if use_letters:
        characters += character_sets['letters']
    if use_numbers:
        characters += character_sets['numbers']
    if use_symbols:
        characters += character_sets['symbols']
    
    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Random Password Generator!")

    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Your generated password is: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
