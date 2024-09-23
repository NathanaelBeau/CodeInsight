df0 = pd.DataFrame({"a": [1, 2, 3, 4], "b": [1, 1, 1, 1], "c": [1000, 2000, 3000, 4000]})
result = test(df0)
expected_output = [(1, [1000]), (2, [2000]), (3, [3000]), (4, [4000])]
assert result == expected_output, 'Test failed'