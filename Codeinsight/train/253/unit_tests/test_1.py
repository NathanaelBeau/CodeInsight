df2 = pd.DataFrame({ 'X': [12, 24, 36], 'Y': [4, 6, 12] })
column_name2 = "Z"
dividend_column2 = "X"
divisor_column2 = "Y"
expected_result2 = pd.DataFrame({ 'X': [12, 24, 36], 'Y': [4, 6, 12], 'Z': [3.0, 4.0, 3.0] })
assert test(df2, column_name2, dividend_column2, divisor_column2).equals(expected_result2), 'Test failed'