df0 = pd.DataFrame({'name': ['pear', 'melon', 'peach', 'plum']})
lst0 = ['melon', 'peach', 'pear', 'plum']
expected_result =  pd.DataFrame({'name': ['melon', 'peach', 'pear', 'plum']})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'