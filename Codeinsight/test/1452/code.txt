def test(dict0):
    sorted_items = sorted(dict0.items(), key=lambda tup: sum(tup[1]), reverse=True)[:3]
    summary = {}
    for key, value in sorted_items:
        summary[key] = sum(value)
    return summary
