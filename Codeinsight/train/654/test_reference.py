def test(lst0):
    groups = {}
    
    for item in lst0:
        prefix = item.split('_')[0]
        if prefix in groups:
            groups[prefix].append(item)
        else:
            groups[prefix] = [item]
    
    return list(groups.values())

