df0 = pd.DataFrame({'M': [100, 200, 300], 'N': [400, 500, 600]}, index=['x', 'y', 'z'])
lst0 = ['x', 'z']
expected_result =  pd.DataFrame({'M': [100, 300], 'N': [400, 600]}, index=['x', 'z'])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'