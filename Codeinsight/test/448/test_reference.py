def test(lst0):
    unique_elements = []
    for item in lst0:
        if item not in unique_elements:
            unique_elements.append(item)
    return sorted(unique_elements)


