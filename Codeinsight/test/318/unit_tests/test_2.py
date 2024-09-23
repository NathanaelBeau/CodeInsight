var2 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'parrot']})
expected_result3 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'bird']})
result3 = test(var2.copy(), 'B', 'parrot', 'bird')
assert result3.equals(expected_result3), 'Test failed'