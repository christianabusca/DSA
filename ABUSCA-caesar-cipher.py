en = 1
dn = 2
quit = 3

def main():
    menu_display()
    choice = 0
    while choice != quit:
        choice = int(input("Enter Your Choice: "))
        if choice == en:
            encryption()
        elif choice == dn:
            decryption()
        elif choice == quit:
            print("Exiting the program")
        else:
            print("Error: Invalid selection")

def encryption():
    user_text = input("Enter the text to be encrypted: ")
    shift_value = 3
    result = caesar_cipher(user_text, shift_value, "encrypt")
    print("Encrypted text:", result)

def decryption():
    user_text = input("Enter the text to be decrypted: ")
    shift_value = -3
    result = caesar_cipher(user_text, shift_value, "decrypt")
    print("Decrypted text:", result)

def caesar_cipher(text, shift, operation):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) + shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char
    return result

def menu_display():
    print("***CAESAR CIPHER***")
    print("Please choose what you want to do.")
    print("1.) Encryption")
    print("2.) Decryption")
    print("3.) Quit")

main()