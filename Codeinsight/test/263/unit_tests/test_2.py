df0 = pd.DataFrame({ ('X', 'Y'): [9, 10], ('X', 'Z'): [11, 12], ('Y', 'Y'): [13, 14], ('Y', 'Z'): [15, 16] })
str0 = 'Z'
expected_result =  pd.DataFrame({ ('X', 'Z'): [11, 12], ('Y', 'Z'): [15, 16] })
result = test(df0, str0)
assert result.equals(expected_result), 'Test failed'