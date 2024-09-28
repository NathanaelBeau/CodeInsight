import pandas as pd
df0 = pd.DataFrame({'Mt': ['A', 'B', 'C'],
                           'count': [5, 5, 5]})
expected_output = pd.DataFrame({'Mt': ['A', 'B', 'C'],
                                        'count': [5, 5, 5]})
result = test(df0)  
sorted_result = result.sort_values('count', ascending=False)
sorted_result = sorted_result.reset_index(drop=True)
expected_output_reset = expected_output.reset_index(drop=True)
assert sorted_result.to_dict() == expected_output_reset.to_dict(), 'Test failed'