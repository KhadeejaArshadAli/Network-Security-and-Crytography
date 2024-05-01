from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return iv + ciphertext

def decrypt_message(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return decrypted_message.decode()

# Example usage
message = input("Enter the message: ")
key = get_random_bytes(16) 
option= int(input("Enter the option 1 for encryption and 2 for decryption:"))
if(option==1):
    encrypted = encrypt_message(message, key)
    print("Encrypted:", encrypted)
elif(option==2):
        encrypted = encrypt_message(message, key)
        decrypted = decrypt_message(encrypted, key)
        print("Encrypted:", encrypted)
    
        print("Decrypted:", decrypted)

    
