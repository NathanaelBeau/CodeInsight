var0 = pd.DataFrame({'A': ['bird', 'fish', 'bird'], 'B': ['grape', 'orange', 'grape']})
expected_result =  pd.DataFrame({'A_bird': [1, 0, 1], 'A_fish': [0, 1, 0], 'B_grape': [1, 0, 1], 'B_orange': [0, 1, 0]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'