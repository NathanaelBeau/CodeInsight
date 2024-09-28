arr0 = np.array([100, 200, 300, 400, 500, 600, 700, 800])
expected_output = np.array([[100, 200], [300, 400], [500, 600], [700, 800]])
assert (test(arr0)  == expected_output).all(), 'Test failed'