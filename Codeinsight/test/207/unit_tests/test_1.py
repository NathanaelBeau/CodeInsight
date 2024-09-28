import pandas as pd 
df0 = pd.DataFrame({'ID': [1, 2, 3],
                    'Salary': [5000, 6000, 7000],
                    'Department': ['HR', 'IT', 'Finance']})
var0 = 'Salary'
var1 = 6000
expected_result =  pd.DataFrame({'ID': [2], 'Salary': [6000], 'Department': ['IT']})
result = test(df0, var0, var1).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'