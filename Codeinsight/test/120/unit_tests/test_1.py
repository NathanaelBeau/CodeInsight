var0 = pd.DataFrame({'Date': ['2020-05-05', '2020-05-15', '2020-05-20', '2020-05-01']})
expected_result =  pd.Series(['2020-05-01', '2020-05-20'], index=['min', 'max'])
result = test(var0)
assert result.equals(expected_result), 'Test failed'