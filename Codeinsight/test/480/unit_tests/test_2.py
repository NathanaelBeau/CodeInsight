df0 = pd.DataFrame({ 'Company': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-01', '2022-01-03', '2022-01-02', '2022-01-01', '2022-01-02', '2022-01-01'], 'value': [10, 20, 30, 40, 50, 60, 70, 80] })
str0 = 'Company'
str1 = 'date'
expected_output = df0.set_index([str0, str1])
assert test(df0, str0, str1) .equals( expected_output), 'Test failed'