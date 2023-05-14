original = input('Please enter a sentence: ').lower()

words = original.split()

new_words = []

for word in words:
    if word[0] in 'aeoiu':
        new_word = word + 'yay'
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeuio':
                vowel_pos +=1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + 'yay'
        new_words.append(new_word)
        pig_words=" ".join(new_words)
print(pig_words)