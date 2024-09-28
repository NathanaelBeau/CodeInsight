df0 = pd.DataFrame({'C': [13, 14, 15]})
arr0 = np.array([16, 17, 18])
expected_result =  pd.DataFrame({'C': [13, 14, 15], 'new_column': [16, 17, 18]})
result = test(df0, arr0)
assert result.equals(expected_result), 'Test failed'