def test(var1):
    words = var1.split(' ')
    rever_word = [ i[::-1] for i in words ]
    final_sen = ' '.join(rever_word)
    return final_sen
