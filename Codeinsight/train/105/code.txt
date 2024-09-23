def test(var1): 
    no_spaces = [char for char in var1 if char!=' ']   
    space= len(var1) - len(no_spaces)
    result = ' '*space    
    return result + ''.join(no_spaces)