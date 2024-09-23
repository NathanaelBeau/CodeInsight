# Test 1
arr0 = np.array([[1, 2, 3], [4, 5, 6]])
lst0 = ["row1", "row2"]
lst1 = ["col1", "col2", "col3"]
expected_result =  pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], index=["row1", "row2"], columns=["col1", "col2", "col3"])
result = test(arr0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'