# Test 2
arr0 = np.array([[10, 20], [30, 40]])
lst0 = ["a", "b"]
lst1 = ["x", "y"]
expected_result =  pd.DataFrame(data=[[10, 20], [30, 40]], index=["a", "b"], columns=["x", "y"])
result = test(arr0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'