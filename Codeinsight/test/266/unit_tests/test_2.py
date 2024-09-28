df0 = pd.DataFrame({'name': ['Peach', 'Mango', 'Berry']})
expected_result =  pd.DataFrame({'name': ['Peach', 'Mango', 'Berry']})
result = test(df0)
assert result.equals(expected_result), 'Test failed'