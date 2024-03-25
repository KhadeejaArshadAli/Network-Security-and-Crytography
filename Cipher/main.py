def Encryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result
def Decryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result

option=int (input("Enter the option 1 for Encryption or 2 for Decryption:"))
plaintext=input("Enter the text you want to encrypt or decrypt:")
shift=int(input("Enter the number of positions by which you want to shift:"))
if option==1:
    ciphertext=Encryption(plaintext,shift)
elif option==2:
    ciphertext=Decryption(plaintext,shift)
else:
    print ("Invalid Option")
print ("Cipher Text is :",ciphertext)


