import pandas as pd
df0 = pd.DataFrame({'id': ['apple', 'banana', 'cherry'], 'value': [5, 3, 8]})
expected_result =  {'apple': 5, 'banana': 3, 'cherry': 8}
assert test(df0) == expected_result, 'Test failed'