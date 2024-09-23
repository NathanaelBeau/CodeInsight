df0 = pd.DataFrame({ 'room': ['X', 'Y'], 'date': ['2022-02-01', '2022-02-02'], 'hour': ['09:00', '10:00'], 'time_x': [10, 20] })
df1 = pd.DataFrame({ 'room': ['X', 'Y'], 'date': ['2022-02-01', '2022-02-02'], 'hour': ['09:00', '10:00'], 'time_y': [30, 40] })
expected_result =  pd.DataFrame({ 'room': ['X', 'Y'], 'date': ['2022-02-01', '2022-02-02'], 'hour': ['09:00', '10:00'], 'time_y': [30, 40] })
assert test(df0, df1) .equals( expected_result), 'Test failed'