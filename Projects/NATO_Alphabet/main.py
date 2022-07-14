import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
letter = []
code = []

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}


word = input("Enter a word: ").upper()
code_list = [phonetic_dict[letter] for letter in word]

print(code_list)