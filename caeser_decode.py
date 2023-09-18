#file: caeser_decode.py
#author: tylerjamesf
#date: September 15, 2023

import time

# ask the user for the message filename
message = input("Enter the message code you wish to decipher: ")

# ask the user for the key offset for cipher
offset = input("Enter the code offset key: ")
elapsed_time = 0
#function to decode
def caeser_cipher(message, offset):

  start_time = time.time()
  
  alphabet_letters = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
  output = ''
  for letter in message:
   if letter in "!?.,' ":
      output += letter
   else:
     output += alphabet_letters[alphabet_letters.find(letter) + offset]
  end_time = time.time()
  elapsed_time = end_time - start_time
  return output, elapsed_time

print("Elapsed time: ", elapsed_time)
print(caeser_cipher(message, offset))