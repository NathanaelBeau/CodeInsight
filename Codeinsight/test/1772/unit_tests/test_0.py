matrix2 = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
expected_output = True
assert test(matrix2) == expected_output, 'Test failed'