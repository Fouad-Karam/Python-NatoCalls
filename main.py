import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_data_frame)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dict["C"])

name = input("Enter your name: ").upper()
output_list = [nato_dict[letter] for letter in name]
print(output_list)
