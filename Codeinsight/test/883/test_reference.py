from collections import Counter

def test(lst0):
    categories_counter = Counter()
    for entry in lst0:
        categories_counter.update(entry['categories'])
    
    return dict(categories_counter)