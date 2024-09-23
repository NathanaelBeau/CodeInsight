df0 = pd.DataFrame({'col1': [-5, 0, 5], 'col2': [-10, 0, 10]})
lst0 = ['col1', 'col2']
expected_result =  pd.DataFrame({'col1': [-5, 0, 5], 'col2': [-10, 0, 10], 'max_value': [-5, 0, 10]})
assert test(df0, lst0).equals(expected_result), 'Test failed'