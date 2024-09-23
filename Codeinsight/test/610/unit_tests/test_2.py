# Test 3
arr0 = np.array([[7, 8, 9], [10, 11, 12]])
lst0 = ["one", "two"]
lst1 = ["alpha", "beta", "gamma"]
expected_result =  pd.DataFrame(data=[[7, 8, 9], [10, 11, 12]], index=["one", "two"], columns=["alpha", "beta", "gamma"])
result = test(arr0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'