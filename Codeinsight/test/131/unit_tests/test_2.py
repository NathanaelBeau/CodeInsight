lst0 = [
            {'a': 1, 'b': 2},
            {'a': 2, 'b': 3},
            {'a': 3, 'b': 4}
        ]
result = test(lst0)
expected = [{'a': 1, 'b': 2}, {'a': 2, 'b': 3}, {'a': 3, 'b': 4}]
result = sorted([sorted(item.items()) for item in result])
expected = sorted([sorted(item.items()) for item in expected])
assert result == expected, 'Test failed'