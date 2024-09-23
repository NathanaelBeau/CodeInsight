var0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'bird']})
expected_result1 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['doggo', 'cat', 'bird']})
result1 = test(var0.copy(), 'B', 'dog', 'doggo')
assert result1.equals(expected_result1), 'Test failed'