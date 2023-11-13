def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
#checks if character is lower or upper case        
        if ord(char) <= 90:
            encrypted_text += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:
            encrypted_text += chr(((ord(char) - 97 + shift) % 26) + 97)
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if ord(char) <= 90:
            decrypted_text += chr(((ord(char) - 65 - shift) % 26) + 65)
        else:
            decrypted_text += chr(((ord(char) - 97 + shift) % 26) + 97)
    return decrypted_text


code = caesar_encrypt("Hello",13)
message = caesar_decrypt(code,13)
print("Hello", "-->", code)
print(code, "-->", message)
