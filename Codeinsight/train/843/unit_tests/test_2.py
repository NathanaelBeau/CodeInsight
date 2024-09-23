df0 = pd.DataFrame({'data': ['apple-orange', 'banana-grape', 'cherry-blueberry']})
expected_result =  pd.DataFrame({0: ['apple', 'banana', 'cherry'], 1: ['orange', 'grape', 'blueberry']})
result = test(df0, 'data', var0='-')
assert result.equals(expected_result), 'Test failed'