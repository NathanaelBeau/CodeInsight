from collections import Counter

def test(lst0):
    counts = Counter(lst0)
    unique_items = []
    for item, count in counts.items():
        if count == 1:
            unique_items.append(item)
    return [item for item in lst0 if item in unique_items]

