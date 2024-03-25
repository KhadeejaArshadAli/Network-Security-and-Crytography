def vigenere_encrypt(text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = alphabet.index(key[key_index].upper())
            if char.islower():
                result += alphabet[(alphabet.index(char.upper()) + shift) % 26].lower()
            else:
                result += alphabet[(alphabet.index(char.upper()) + shift) % 26]
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = alphabet.index(key[key_index].upper())
            if char.islower():
                result += alphabet[(alphabet.index(char.upper()) - shift) % 26].lower()
            else:
                result += alphabet[(alphabet.index(char.upper()) - shift) % 26]
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

plaintext=input("Enter the plaintext : ")
key=input("Enter the key : ")
option=input("ENCRYPT OR DECRYPT OR BOTH:")
if option=='BOTH':
 print('Encrypted Text is ',vigenere_encrypt(plaintext,key))
 print('Decrypted Text is ',vigenere_decrypt(vigenere_encrypt(plaintext,key),key))
elif option=="ENCRYPT":
    print('Encrypted Text is ',vigenere_encrypt(plaintext,key))
elif option=="DECRYPT":
    print('Dencrypted Text is ',vigenere_decrypt(plaintext,key))
else:
    print('Check option please')
          

