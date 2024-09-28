import pandas as pd
def concatenate_strings(row):
    return row['text1'] + row['text2']
var0 = concatenate_strings
var1 = 'concatenation'
df0 = pd.DataFrame({'text1': ['Hello', 'Goodbye'], 'text2': [' World', ' Universe']})
expected_result =  pd.DataFrame({'text1': ['Hello', 'Goodbye'], 'text2': [' World', ' Universe'], 'concatenation': ['Hello World', 'Goodbye Universe']})
result = test(var0, var1, df0)
assert result.equals(expected_result), 'Test failed'