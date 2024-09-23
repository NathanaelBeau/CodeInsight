var1 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'bird']})
expected_result2 = pd.DataFrame({'A': ['apple pie', 'banana', 'cherry'], 'B': ['dog', 'cat', 'bird']})
result2 = test(var1.copy(), 'A', 'apple', 'apple pie')
assert result2.equals(expected_result2), 'Test failed'