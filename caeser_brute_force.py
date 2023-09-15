#file: caeser_brute_force.py
#author: tylerjamesf
#date: September 15, 2023

# ask the user for the message to brute force decode
message = input("Enter the message you want to brute force decode: ")

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

# iterate over each possible key to brute force
for i in range(27):
  print(caeser_cipher(message, i))
  print("The offset key used: " + str(i))