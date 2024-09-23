def test(lst0):
    result = {}
    for d in lst0:
        for k, v in d.items():
            result[k] = result.get(k, 0) + v
    sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
    return sorted_result

