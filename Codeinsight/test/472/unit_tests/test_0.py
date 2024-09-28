df0 = pd.DataFrame({"A": ["apple", "apple", "banana"], "B": ["red", "green", "red"]})
col1 = "A"
col2 = "B"
expected_output = [("apple", "green", 1), ("apple", "red", 1), ("banana", "red", 1)]
assert sorted(test(df0, col1, col2)) == sorted(expected_output), 'Test failed'