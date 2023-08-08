import random

def encrypt_word(word):
    if len(word) >= 3:
        new_word = word[1:] + word[0]
        random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        encrypted_word = random_chars + new_word + random_chars
    else:
        encrypted_word = word

    return encrypted_word

def decrypt_word(word):
    if len(word) >= 6:
        new_word = word[3:-3]
        decrypted_word = new_word[-1] + new_word[:-1]
    else:
        decrypted_word = word

    return decrypted_word

def main():
    print("Welcome to the Word Encryption/Decryption Program!")

    sentence = input("Enter a sentence: ")
    words = sentence.split()

    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()

    if choice == 'E':
        encrypted_words = [encrypt_word(word) for word in words]
        encrypted_sentence = ' '.join(encrypted_words)
        print(f"Encrypted sentence: {encrypted_sentence}")
    elif choice == 'D':
        decrypted_words = [decrypt_word(word) for word in words]
        decrypted_sentence = ' '.join(decrypted_words)
        print(f"Decrypted sentence: {decrypted_sentence}")
    else:
        print("Invalid choice. Please enter 'E' or 'D' only.")

if __name__ == "__main__":
    main()
