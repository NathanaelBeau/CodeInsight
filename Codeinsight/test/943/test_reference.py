import heapq

def test(dict0):
    largest_items = heapq.nlargest(3, dict0.items(), key=lambda tup: sum(tup[1]))
    summary = {}
    for key, value in largest_items:
        summary[key] = sum(value)
    return summary
