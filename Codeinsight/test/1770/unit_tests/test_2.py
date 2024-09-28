df3 = pd.DataFrame({'Label': ['X', 'Y'], 'Data1': [11, 14], 'Data2': [12, 15]})
expected_result3 = pd.DataFrame({'X': [11, 12], 'Y': [14, 15]}, index=['Data1', 'Data2'])
result3 = test(df3, 'Label')
assert result3.equals(expected_result3), 'Test failed'