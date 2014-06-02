import string

letters = string.ascii_uppercase

vigenere_table = {letter: {letters[j]: letters[(i + j) % 26]
                           for j, l in enumerate(letters)}
                  for i, letter in enumerate(letters)}


def decrypt(text, key):
  decrypt = []
  for index, letter in enumerate(key):
    for plain in vigenere_table[letter]:
      if vigenere_table[letter][plain] == text[index]:
        decrypt.append(plain)
  return ''.join(decrypt)


def encrypt(text, key):
  encrypted = []
  for index, letter in enumerate(text):
    encrypted.append(vigenere_table[letter][key[index]])
  return ''.join(encrypted)

TEXT = "ATTACKATDAWN"
KEY = "LEMONLEMONLE"

print encrypt(TEXT, KEY)
print decrypt(encrypt(TEXT, KEY), KEY)
