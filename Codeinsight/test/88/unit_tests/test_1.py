df0 = pd.DataFrame({'name': ['orange', 'grape', 'kiwi', 'mango']})
lst0 = ['kiwi', 'mango', 'orange', 'grape']
expected_result =  pd.DataFrame({'name': ['kiwi', 'mango', 'orange', 'grape']})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'