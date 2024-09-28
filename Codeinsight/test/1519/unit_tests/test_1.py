var0 = pd.DataFrame({'A': [13, 14, 15, 16, 17, 18], 'B': [19, 20, 21, 22, 23, 24]})
n = 3
expected_result =  pd.DataFrame({'A': [13, 16], 'B': [19, 22]})
result = test(var0, n).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'