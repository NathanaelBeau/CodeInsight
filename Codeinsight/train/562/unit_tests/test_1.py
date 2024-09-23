str0 = b'\x00\x00\x00\x00'
expected_output = np.array([0.0], dtype=np.float32)
assert test(str0) ==expected_output, 'Test failed'