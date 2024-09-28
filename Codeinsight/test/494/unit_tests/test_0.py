lst0 = [
            {'a': 1, 'b': 2},
            {'b': 2, 'a': 1},  # same content, different order
            {'a': 1, 'b': 3},
            {'a': 1, 'b': 2}   # duplicate of the first dict
        ]
result = test(lst0)
expected = [{'a': 1, 'b': 2}, {'a': 1, 'b': 3}, {'b': 2, 'a': 1}]
result = sorted([sorted(item.items()) for item in result])
expected = sorted([sorted(item.items()) for item in expected])
assert result == expected, 'Test failed'