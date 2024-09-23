df3 = pd.DataFrame({'P': [None, 45., None, 80.], 'Q': [100., 110., 120., 130.]})
expected_result =  pd.DataFrame({'P': [100., 45., 120., 80.], 'Q': [100., 110., 120., 130.]})
result = test(df3, 'P', 'Q')
assert result .equals( expected_result), 'Test failed'