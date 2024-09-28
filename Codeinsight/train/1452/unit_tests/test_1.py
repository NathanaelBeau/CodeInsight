df0 = pd.DataFrame({'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 35]}, index=['ID1', 'ID2', 'ID3'])
expected_output = ['ID1', 'ID2', 'ID3']
assert test(df0) ==expected_output, 'Test failed'