import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df0 = pd.DataFrame(data, index=[0, 1, 0])
expected_result =  pd.DataFrame({'A': [1, 2], 'B': [4, 5]}, index=[0, 1])
result = test(df0)
assert result.equals(expected_result), 'Test failed'