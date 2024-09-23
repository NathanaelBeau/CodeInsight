ser0 = pd.Series(['apple', 'banana', 'cherry'], index=['a', 'b', 'c'])
expected_result =  'apple'
result = test(ser0)
assert result == expected_result, 'Test failed'