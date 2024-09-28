var0 = pd.DataFrame({'Date': ['2019-12-31', '2020-01-01', '2020-01-02']})
expected_result =  pd.Series(['2019-12-31', '2020-01-02'], index=['min', 'max'])
result = test(var0)
assert result.equals(expected_result), 'Test failed'