def test(str0, var0):
    if len(str0) <= var0:
        return [str0]

    words = str0.split()  
    result = []
    current_chunk = words[0]  

    for word in words[1:]:
        
        if len(current_chunk) + len(word) + 1 <= var0:
            current_chunk += ' ' + word
        else:
            result.append(current_chunk)
            current_chunk = word

    result.append(current_chunk)
    return result
