df1 = pd.DataFrame({ 'Name': ['John', 'Jane', 'Mike'], 'Age': [25, 30, 35] })
expected_result1 = pd.DataFrame({ 'Name': ['John', 'Jane', 'Mike'], 'Age': [25, 100, 35] })
result1 = test(df1, 'Name', 'Jane', 'Age', 100)
assert result1.equals(expected_result1), 'Test failed'