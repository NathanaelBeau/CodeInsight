def test(lst0, lst1):
    order = {item: i for i, item in enumerate(lst1)}
    return sorted(lst0, key=lambda x: order.get(x, -1))