#file: caeser_decode.py
#author: tylerjamesf
#date: September 15, 2023

# ask the user for the message filename
message = input("Enter the message code you wish to decipher: ")

# ask the user for the key offset for cipher
offset = input("Enter the code offset key: ")

#function to decode
def caeser_cipher(message, offset):
  
  alphabet_letters = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
  output = ''
  for letter in message:
   if letter in "!?.,' ":
      output += letter
   else:
     output += alphabet_letters[alphabet_letters.find(letter) + offset]
  return output

print(caeser_cipher(message, offset))