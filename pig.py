original = input('Please enter a sentence: ').lower()

words = original.split()

new_words = []

for word in words:
    if word[0] in 'aeoiu':
        new_word = word + 'yay'
        new_words.append(new_word)
        
