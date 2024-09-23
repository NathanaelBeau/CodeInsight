df1 = pd.DataFrame({ 'A': [10, 20, 30], 'B': [2, 5, 10] })
column_name = "C"
dividend_column = "A"
divisor_column = "B"
expected_result1 = pd.DataFrame({ 'A': [10, 20, 30], 'B': [2, 5, 10], 'C': [5.0, 4.0, 3.0] })
assert test(df1, column_name, dividend_column, divisor_column).equals(expected_result1), 'Test failed'