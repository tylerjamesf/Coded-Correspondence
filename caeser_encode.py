#file: caeser_encode.py
#author: tylerjamesf
#date: September 15, 2023

# ask the user for the message filename
message = input("Enter the message you want to encode: ")

# ask the user for the key offset for cipher
offset = int(input("Enter the offset number key to use: "))

#function to encode
def caeser_cipher(message, offset):
  
  alphabet_letters = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
  output = ''
  for letter in message:
   if letter in "!?.,' ":
      output += letter
   else:
     output += alphabet_letters[alphabet_letters.find(letter) - offset]
  return output

print(caeser_cipher(message, offset))