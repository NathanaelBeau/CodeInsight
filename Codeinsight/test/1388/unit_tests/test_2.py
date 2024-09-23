df0 = pd.DataFrame({"M": ["blue", "red", "blue", "blue"], "N": ["circle", "circle", "triangle", "circle"]})
col1 = "M"
col2 = "N"
expected_output = [("blue", "circle", 2), ("blue", "triangle", 1), ("red", "circle", 1)]
assert sorted(test(df0, col1, col2)) == sorted(expected_output), 'Test failed'