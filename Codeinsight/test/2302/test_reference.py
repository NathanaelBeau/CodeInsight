def recursive_split(sentence, n):
    if not sentence:
        return []

    if len(sentence) <= n:
        return [sentence]

  
    if sentence[n] == ' ':
        return [sentence[:n]] + recursive_split(sentence[n+1:], n)
    else:
        
        idx = sentence.rfind(' ', 0, n)
        if idx == -1:  
            space_idx = sentence.find(' ')
            if space_idx == -1:  
                return [sentence]
            else:
                return [sentence[:space_idx]] + recursive_split(sentence[space_idx+1:], n)
        else:
            return [sentence[:idx]] + recursive_split(sentence[idx+1:], n)


def test(str0, var0):
    return recursive_split(str0, var0)