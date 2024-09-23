import itertools

def test(lst0, var0):
    if var0 == 0:
        return ['']
    
    result = []
    for i, token in enumerate(lst0):
        remaining_tokens = lst0[:i] + lst0[i + 1:]
        for combination in test(remaining_tokens, var0 - 1):
            result.append(token + combination)
    
    return result


