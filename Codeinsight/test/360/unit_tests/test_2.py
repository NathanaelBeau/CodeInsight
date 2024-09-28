df0 = pd.DataFrame({ 'room': ['X', 'Y', 'Z'], 'date': ['2022-02-01', '2022-02-02', '2022-02-03'], 'hour': ['08:00', '09:00', '10:00'], 'time_x': [10, 20, 30] })
df1 = pd.DataFrame({ 'room': ['X', 'Y', 'Z'], 'date': ['2022-02-01', '2022-02-02', '2022-02-03'], 'hour': ['08:00', '09:00', '10:00'], 'time_y': [40, 50, 60] })
expected_result =  pd.DataFrame({ 'room': ['X', 'Y', 'Z'], 'date': ['2022-02-01', '2022-02-02', '2022-02-03'], 'hour': ['08:00', '09:00', '10:00'], 'time_y': [40, 50, 60] })
assert test(df0, df1) .equals( expected_result), 'Test failed'