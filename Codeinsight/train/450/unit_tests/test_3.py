import pandas as pd 
df4 = pd.DataFrame([[3, 6, 9], [2, 4, 6]])
expected_result4 = pd.DataFrame([[0.166667, 0.333333, 0.5], [0.166667, 0.333333, 0.5]])
result4 = test(df4)
expected_result_rounded = expected_result4.round(6)
result_rounded = result4.round(6)
assert result_rounded.equals(expected_result_rounded), 'Test failed'