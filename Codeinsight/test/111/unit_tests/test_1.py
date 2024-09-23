var0 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
expected_result2 = pd.DataFrame({'A': [0.4166666666666667, 0.42857142857142855], 'B': [0.5833333333333334, 0.5714285714285714]})
result2 = test(var0)
assert result2.equals(expected_result2), 'Test failed'