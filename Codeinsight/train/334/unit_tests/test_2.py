# Unit Test 3
dict0 = {'P': [13, 14, 15], 'Q': [16, 17, 18]}
expected_result =  pd.DataFrame({'P': [13, 14, 15], 'Q': [16, 17, 18]})
result = test(dict0)
assert result.equals(expected_result), 'Test failed'