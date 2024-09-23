arr2 = np.array([0, 0, 0, 6])
expected_result =  arr2 / np.linalg.norm(arr2)
result = test(arr2)
assert np.allclose(result, expected_result), 'Test failed'