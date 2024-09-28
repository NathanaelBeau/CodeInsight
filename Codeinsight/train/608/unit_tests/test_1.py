# Unit Test 3
df0 = pd.DataFrame({ ('P', 'q1'): [13, 14], ('P', 'q2'): [15, 16], ('Q', 'q3'): [17, 18] })
expected_result =  pd.DataFrame({ 'P q1': [13, 14], 'P q2': [15, 16], 'Q q3': [17, 18] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'