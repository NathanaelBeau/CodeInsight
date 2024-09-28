df2 = pd.DataFrame({'ID': [101, 102], 'Score1': [85, 90], 'Score2': [88, 92]})
expected_result2 = pd.DataFrame({101: [85, 88], 102: [90, 92]}, index=['Score1', 'Score2'])
result2 = test(df2, 'ID')
assert result2.equals(expected_result2), 'Test failed'