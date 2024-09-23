var0 = pd.DataFrame({ 'X': ['Y', '5', '6'], 'Z': ['W', '7', '8'] })
expected_result =  pd.DataFrame({ 'Y': ['5', '6'], 'W': ['7', '8'] }, index=[1, 2])
result = test(var0)
assert result.equals(expected_result), 'Test failed'