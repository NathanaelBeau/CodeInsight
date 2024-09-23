# Test 3
df0 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [50., -np.inf, 70., 80.]})
var0 = 'Score'
expected_result =  pd.DataFrame({'Name': ['Alice', 'Charlie', 'David'], 'Score': [50., 70., 80.]})
result = test(df0, var0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'