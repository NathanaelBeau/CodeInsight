a = sorted(test([{"a": 1, "b": 2, "c": 3}, {"c": 3, "a": 1, "b": 2}, {"b": 2, "a": 1, "c": 3}]), key = lambda ele: sorted(ele.items())) 
b = sorted([{"a": 1, "b": 2, "c": 3}], key = lambda ele: sorted(ele.items()))
assert a == b, 'Test failed'