# Unit Test 2
df0 = pd.DataFrame(columns=['Name', 'Age'])
expected_result =  True
result = test(df0)
assert result == expected_result, 'Test failed'