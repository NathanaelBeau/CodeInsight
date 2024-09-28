arr0 = np.array([10, 20])
arr1 = np.array([1, 2, 3, 4])
expected_output = np.array([[10, 20, 30, 40],
                            [20, 40, 60, 80]])
assert (test(arr0, arr1)  == expected_output).all(), 'Test failed'