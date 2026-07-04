def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result

def decrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result

def get_shift():
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            print("Shift must be between 1 and 25")
        except ValueError:
            print("Please enter a valid number")

def get_message():
    while True:
        message = input("Enter message: ").strip()
        if message:
            return message
        print("Message cannot be empty")

def main():

    print("=" * 40)
    print("      CAESAR CIPHER PROGRAM")
    print("=" * 40)

    while True:

        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            message = get_message()
            shift = get_shift()
            encrypted = encrypt(message, shift)
            print("\nOriginal Message :", message)
            print("Shift Value      :", shift)
            print("Encrypted Text   :", encrypted)

        elif choice == "2":
            message = get_message()
            shift = get_shift()
            decrypted = decrypt(message, shift)
            print("\nOriginal Message :", message)
            print("Shift Value      :", shift)
            print("Decrypted Text   :", decrypted)

        elif choice == "3":

            print("Thank you")
            break

        else:
            print("Invalid choice")


main()