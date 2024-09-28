# Test for an empty DataFrame
df_empty = pd.DataFrame(columns=['A', 'B'])
result_empty = test(df_empty)
expected_empty = []

assert result_empty.tolist() == expected_empty, f"Test Failed"
