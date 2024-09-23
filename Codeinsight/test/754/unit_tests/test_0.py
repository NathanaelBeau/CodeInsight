import pandas as pd 
df0 = pd.DataFrame({'Name': ['John', 'Alice', 'Bob'],
                    'Age': [25, 30, 35],
                    'City': ['New York', 'London', 'Paris']})
var0 = 'Name'
var1 = 'Alice'
expected_result =  pd.DataFrame({'Name': ['Alice'], 'Age': [30], 'City': ['London']}, index=[1])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'