def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    text = input("Введите текст: ")
    shift = int(input("Введите шаг сдвига: "))

    encrypted_text = encrypt(text, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print(f"Зашифрованный текст: {encrypted_text}")
    print(f"Расшифрованный текст: {decrypted_text}")

if __name__ == "__main__":
    main()