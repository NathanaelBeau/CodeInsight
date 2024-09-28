df0 = pd.DataFrame( np.random.randn(8, 4), index=pd.date_range('1/1/2000', periods=8), columns=['A', 'B', 'C', 'D'] )
str0 = '2000-01-03'
expected_output = 2
assert test(df0, str0) ==expected_output, 'Test failed'