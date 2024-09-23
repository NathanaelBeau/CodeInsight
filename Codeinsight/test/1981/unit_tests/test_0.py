df0 = pd.DataFrame({'A': ['apple', 'banana'], 'B': ['cherry', 'date']})
str0 = 'banana'
expected_output = True
assert test(str0, df0) == expected_output, 'Test failed'