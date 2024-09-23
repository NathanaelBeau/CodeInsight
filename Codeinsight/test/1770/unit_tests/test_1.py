df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'elephant']})
lst0 = ['elephant', 'dog', 'cat']
var0 = 'B'
expected_result_2 = pd.DataFrame({'A': ['cherry', 'apple', 'banana'], 'B': ['elephant', 'dog', 'cat']}).reset_index(drop=True)
result_2 = test(df0, lst0, var0).reset_index(drop=True)
assert result_2.equals(expected_result_2), 'Test failed'