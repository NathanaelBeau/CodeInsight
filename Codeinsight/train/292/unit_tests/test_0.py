df0 = pd.DataFrame({'X': ['A', 'A', 'B', 'B'],
                           'X2': ['C', 'D', 'C', 'D'],
                           'Value': [1, 2, 3, 4]})
expected_output = pd.pivot_table(df0, index=['X2'], columns=['X'], values='Value', aggfunc=np.sum)
result = test(df0, ['X2'], ['X'], np.sum)
assert result.values.tolist() ==expected_output.values.tolist(), 'Test failed'