import pandas as pd
from english_words import english_words_lower_alpha_set

possibilities = [word for word in english_words_lower_alpha_set if len(word) == 5] # Set the imported word list to lengths of 5

poss_2 = pd.DataFrame({
    'words':possibilities
})
guesses = ['first', 'second', 'third', 'fourth', 'fifth', 'last']
for i in guesses:
    print('What\'s your ' + i + ' guess?')
    print('Type \'end\' to quit')

    word = input()
    if word == 'end':
        break
    else:
        print('''
        What was the feedback?
        Place (b) or (y) or (g) for letters in their 
        correct place.
        ''')
    feedback = input() #bgybb
    #Write for loop such that it looks at both letter placement of the b g y and uses an embedded if statement
    #to evaluate what to do with the b g y by position in the feedback and references the index back to the 
    #guess.
    #This may allow for only one for loop with three if conditions: b g or y by position
    for j in range(5):
        fb_result = feedback[j]
        word_letter = word[j]
        if fb_result == 'b':
            mask = poss_2['words'].str.contains(word_letter)
            poss_2 = poss_2[~mask]
        elif fb_result == 'y':
            mask = poss_2['words'].str.contains(word_letter)
            poss_2 = poss_2[mask]
            mask = poss_2['words'].str[j].str.contains(word_letter)
            poss_2 = poss_2[~mask]
        else:
            mask = poss_2['words'].str[j].str.contains(word_letter)
            poss_2 = poss_2[mask]
        
    print('''
    Here are some remaining choices
    in case you need some help, Granny.
    ''')
    print(poss_2.head())

