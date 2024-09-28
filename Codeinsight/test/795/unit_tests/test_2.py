arr0 = np.array([[100],[200],[300]])
lst0 = ['one', 'two', 'three']
lst1 = ['value']
expected_result =  pd.DataFrame(arr0, index=lst0, columns=lst1)
result = test(arr0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'