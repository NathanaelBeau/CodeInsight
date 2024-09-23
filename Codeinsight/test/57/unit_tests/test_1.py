import pandas as pd 
df0 = pd.DataFrame([[1, 2, 3]])
expected_result =  pd.DataFrame([[0.166667, 0.333333, 0.5]])
result = test(df0)
expected_result_rounded = expected_result.round(6)
result_rounded = result.round(6)
assert result_rounded.equals(expected_result_rounded), 'Test failed'