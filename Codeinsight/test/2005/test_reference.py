def test(lst0):
    groups = []
    seen = set()

    for item in lst0:
        prefix = item.split('_')[0]
        if prefix not in seen:
            seen.add(prefix)
            groups.append([item])
        else:
            for group in groups:
                if group[0].startswith(prefix):
                    group.append(item)
                    break

    return groups

