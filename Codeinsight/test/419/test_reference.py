def test(lst0):
    max_index = 0
    max_value = lst0[0]['size']
    
    for index, item in enumerate(lst0):
        if item['size'] > max_value:
            max_index = index
            max_value = item['size']
    
    return max_index

