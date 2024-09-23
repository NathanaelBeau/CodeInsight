var0 = pd.DataFrame({'A': ['cat', 'dog', 'cat'], 'B': ['apple', 'banana', 'apple']})
expected_result =  pd.DataFrame({'A_cat': [1, 0, 1], 'A_dog': [0, 1, 0], 'B_apple': [1, 0, 1], 'B_banana': [0, 1, 0]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'