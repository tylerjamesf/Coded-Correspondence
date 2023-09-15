#caeser_decode

# ask the user for the message filename
message = input("Enter the message code you wish to decipher: ")
offset = input("Enter the code offset key: ")

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