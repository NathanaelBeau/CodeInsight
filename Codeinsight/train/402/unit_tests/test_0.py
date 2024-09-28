var0 = pd.DataFrame({'Date': ['2022-01-01', '2022-01-10', '2022-01-15']})
expected_result =  pd.Series(['2022-01-01', '2022-01-15'], index=['min', 'max'])
result = test(var0)
assert result.equals(expected_result), 'Test failed'