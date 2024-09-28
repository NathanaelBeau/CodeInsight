import pandas as pd 
df3 = pd.DataFrame([[1, 1], [2, 2]])
expected_result3 = pd.DataFrame([[0.5, 0.5], [0.5, 0.5]])
result3 = test(df3)
assert result3.equals(expected_result3), 'Test failed'