df0 = pd.DataFrame({'col': ['apple', 'banana', 'cherry']})
str0 = 'fruit_'
expected_result =  pd.DataFrame({'col': ['fruit_apple', 'fruit_banana', 'fruit_cherry']})
assert test(df0, 'col', str0).equals(expected_result), 'Test failed'