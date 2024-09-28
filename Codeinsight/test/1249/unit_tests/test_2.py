import pandas as pd
df0 = pd.DataFrame({'A': [0, 0, 0], 'B': [0, 0, 0], 'C': [0, 0, 0]})
expected_result =  pd.DataFrame(index=[0, 1, 2])
assert test(df0).equals(expected_result), 'Test failed'