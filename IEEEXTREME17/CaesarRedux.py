def encrypt_text(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            char_code = ord(char) - 97 
            encrypted_code = (char_code - shift) % 26
            encrypted_char = chr(encrypted_code + 97)  
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text
            
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            char_code = ord(char) - 97  
            decrypted_code = (char_code + shift) % 26
            decrypted_char = chr(decrypted_code + 97)  
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text
       

n = int(input())
for i in range(n):
	k = int(input())
	s = input()
	if ("the" in s.split()):
		print(encrypt_text(s, k))
	else:
		print(decrypt(s, k))
  
  
  
