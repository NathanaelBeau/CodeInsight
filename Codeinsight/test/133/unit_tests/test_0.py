df0 = pd.DataFrame({"a": [3, 4, 3, 5], "b": [2, 2, 2, 6], "c": [3, 4, 1, 6]})
result = test(df0)
expected_output = [(3, [3, 1]), (4, [4]), (5, [6])]
assert result==expected_output, 'Test failed'