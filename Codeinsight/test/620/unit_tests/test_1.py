arr1 = np.array([4, 5])
expected_result =  arr1 / np.linalg.norm(arr1)
result = test(arr1)
assert np.allclose(result, expected_result), 'Test failed'