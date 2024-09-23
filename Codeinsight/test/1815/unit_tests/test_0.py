# Test 1: Regular case
df_test_1 = pd.DataFrame({
    'A': [1, 2],
    'B': ['x,y', 'z,w'],
    'C': [3, 4]
})
result_1 = test(df_test_1, 'B', ',', ['A', 0, 1, 'C'])
expected_1 = pd.DataFrame({'A': [1, 2], 0: ['x', 'z'], 1: ['y', 'w'], 'C': [3, 4]})
assert result_1.equals(expected_1), 'Test failed'