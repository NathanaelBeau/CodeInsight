df0 = pd.DataFrame({ 'A': ['apple', 'apple', 'banana', 'banana', 'cherry', 'cherry'], 'B': [1, 2, 3, 4, 5, 6], 'C': ['p', 'q', 'r', 's', 't', 'u'] })
var0 = 'A'
expected_result1 = pd.DataFrame({ 'A': ['apple', 'banana', 'cherry'], 'B': [1, 3, 5], 'C': ['p', 'r', 't'] })
result1 = test(df0, var0)
assert result1.equals(expected_result1), 'Test failed'