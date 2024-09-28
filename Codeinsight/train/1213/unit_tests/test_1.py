var0= 'name'
df0 = pd.DataFrame({'name': ['(Apple)', '(Banana)', '(Cherry)']})
expected_result =  pd.DataFrame({'name': ['', '', '']})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'