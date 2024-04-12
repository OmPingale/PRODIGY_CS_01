def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_text = caesar_cipher_encrypt(text, shift)
    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
    
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
