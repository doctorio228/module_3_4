def single_root_words(root_word,*other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for word in other_words: 
        lower_word = word.lower()
        if root_word_lower in lower_word or lower_word in root_word_lower: 
            same_words.append(word)
    return same_words
    
print(single_root_words('ТеСт', 'Тестировщик', "травма"))
