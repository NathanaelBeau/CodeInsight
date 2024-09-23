df0 = pd.DataFrame({"X": ["cat", "cat", "dog", "dog"], "Y": ["small", "big", "big", "big"]})
col1 = "X"
col2 = "Y"
expected_output = [("cat", "big", 1), ("cat", "small", 1), ("dog", "big", 2)]
assert sorted(test(df0, col1, col2)) == sorted(expected_output), 'Test failed'