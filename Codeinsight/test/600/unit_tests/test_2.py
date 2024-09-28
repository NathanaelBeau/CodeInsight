df_single_row = pd.DataFrame({
    'A': [1],
    'B': [2]
})
result_single_row = test(df_single_row)
expected_single_row = [1, 2]
assert result_single_row.tolist() == expected_single_row, f"Test Failed"
