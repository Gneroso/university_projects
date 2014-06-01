import string

letters = string.ascii_uppercase

vigenere_table = {letter: {letters[j]: letters[(i + j) % 26]
                           for j, l in enumerate(letters)}
                  for i, letter in enumerate(letters)}


def encrypt(text, key):
  encrypted = []
  for index, letter in enumerate(text):
    encrypted.append(vigenere_table[letter][key[index]])
  return ''.join(encrypted)

TEXT = "ATTACKATDAWN"
KEY = "LEMONLEMONLE"

print encrypt(TEXT, KEY)
