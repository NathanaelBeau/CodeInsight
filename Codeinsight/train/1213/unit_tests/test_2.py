var0= 'name'
df0 = pd.DataFrame({'name': ['Peach', 'Mango', 'Berry']})
expected_result =  pd.DataFrame({'name': ['Peach', 'Mango', 'Berry']})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'