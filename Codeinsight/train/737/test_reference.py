def test(lst0):
    seen_first_components = set()
    result = []
    
    for item in lst0:
        first_component = item[0]
        if first_component not in seen_first_components:
            seen_first_components.add(first_component)
            result.append(item)
    
    return result
