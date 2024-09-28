df3 = pd.DataFrame({'Name': ['John', 'Jane', 'Mike'], 'Age': [30, 25, 40]})
expected_result3 = [['John', 30], ['Jane', 25], ['Mike', 40]]
result3 = test(df3)
assert result3 == expected_result3, 'Test failed'