import pandas as pd
from english_words import english_words_lower_alpha_set

possibilities = [word for word in english_words_lower_alpha_set if len(word) == 5] # Set the imported word list to lengths of 5
type(possibilities)
len(possibilities)

poss_2 = pd.DataFrame({
    'words':possibilities
})
print('What\'s your first guess?')
first_word = input()
print('''
What was the feedback?
Place a (b) or (y) or (g) for letters in their 
correct place.
''')
feedback_1 = input()

