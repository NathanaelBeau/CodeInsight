df0 = pd.DataFrame({ 'room': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'hour': ['10:00', '11:00', '12:00'], 'time_x': [1, 2, 3] })
df1 = pd.DataFrame({ 'room': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'hour': ['10:00', '11:00', '12:00'], 'time_y': [4, 5, 6] })
expected_result =  pd.DataFrame({ 'room': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'hour': ['10:00', '11:00', '12:00'], 'time_y': [4, 5, 6] })
assert test(df0, df1) .equals(expected_result), 'Test failed'