df3 = pd.DataFrame({'C': [True, False, True, True, False, False]})
expected_result3 = pd.Series({True: 3, False: 3}, name='C')
result3 = test(df3, 'C')
assert result3.equals(expected_result3), 'Test failed'