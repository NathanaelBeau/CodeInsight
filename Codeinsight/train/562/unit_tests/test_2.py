str0 = b'\x00\x00\x80?\x00\x00\x00@\x00\x00@@'
expected_output = np.array([1.0, 2.0, 3.0], dtype=np.float32)
assert (test(str0)  == expected_output).all(), 'Test failed'