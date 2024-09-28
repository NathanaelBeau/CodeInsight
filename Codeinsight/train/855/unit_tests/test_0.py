df0 = pd.DataFrame({'name': ['Banana', 'Apple', 'Cherry'], 'value': [2, 1, 3]})
lst0 = ['Apple', 'Banana', 'Cherry']
expected_result =  pd.DataFrame({'name': ['Apple', 'Banana', 'Cherry'], 'value': [1, 2, 3]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'