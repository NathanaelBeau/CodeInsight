df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'elephant']})
lst0 = ['cherry', 'banana', 'apple']
var0 = 'A'
expected_result_1 = pd.DataFrame({'A': ['cherry', 'banana', 'apple'], 'B': ['elephant', 'cat', 'dog']}).reset_index(drop=True)
result_1 = test(df0, lst0, var0).reset_index(drop=True)
assert result_1.equals(expected_result_1), 'Test failed'