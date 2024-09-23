arr0 = np.array([[10,11],[20,21]])
lst0 = ['A', 'B']
lst1 = ['X', 'Y']
expected_result =  pd.DataFrame(arr0, index=lst0, columns=lst1)
result = test(arr0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'