#file: vigenere_decode.py
#author: tylerjamesf
#date: September 15, 2023

#can't figure out how to handle spaces - tf

# ask user for the message to decode
message = input("Enter the message to be decoded: ")

# ask user for the key phrase used
key = input("Enter the key phrase to use for decoding: ")

def decode_vis(message, keyword):
  
  #format inputs to all lowercase to handle string
  message = message.lower()
  keyword = keyword.lower()
  alphabet_letters = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
  output = ''

  #create empty lists to use throughout
  list_1 = []
  list_2 = []
  list_3 = []

  #set range for keyword and total length
  i = 0
  keyword_length = (len(keyword) - 1)

#loop through message and set alphabet key, skip over spaces and other symbols
  for n in message:
    if n in "!?.,' ":
      continue
    else:
      list_1.append(alphabet_letters.find(n))

#loop through message and set keyword letters, skip over spaces and other symbols
  for n in message:
      if i > keyword_length:
        i = 0
        list_2.append(keyword[i])
        i += 1
      elif n in "!?.,' ":
        continue
      else:
        list_2.append(keyword[i])
        i += 1

#loop over new list 2 and set key for friends
  for n in range(len(list_2)):
    list_2[n] = alphabet_letters.find(list_2[n])

#list comprehension to sum the two numbers and set to new list
  list_3 = [(x[0] + x[1]) for x in zip(list_1, list_2)]

#loop through final list and get letters from offset numbers
  for n in list_3:
    output += alphabet_letters[n]
    output += ' '

  return output

print(decode_vis(message, key))