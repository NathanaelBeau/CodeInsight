# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane', 'Doe']})
df1 = pd.DataFrame({'age': [30, 25, 40], 'city': ['NY', 'LA', 'SF']})
expected_result =  pd.DataFrame({'name': ['John', 'Jane', 'Doe'], 'name_age': [30, 25, 40], 'name_city': ['NY', 'LA', 'SF']})
result = test(df0, df1, ['name_age', 'name_city'], ['age', 'city'])
assert result.equals(expected_result), 'Test failed'