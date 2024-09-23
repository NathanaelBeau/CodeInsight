def test(str0):
    words = []
    current_word = ""
    
    for char in str0:
        if char != " ":
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    
    if current_word:
        words.append(current_word)
    
    return words

