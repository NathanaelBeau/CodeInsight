var0 = 'name'
df0 = pd.DataFrame({'name': ['ALICE', 'BOB', None, 'DAVID']})
expected_result =  pd.DataFrame({'name': ['alice', 'bob', None, 'david']})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'