arr0 = np.array([[0.0, 0.0], [0.3, 0.0], [1.25, -0.1], [2.1, -0.9], [2.85, -2.3]])
expected_output = np.array([[0.32500159, -0.04996018], [0.30595746, -0.2231593],
                               [0.11739858, -0.53941179], [-0.06587281, -0.47914917],
                               [-0.04963021, -0.299768]])
acceleration = test(arr0)
assert np.allclose(acceleration, expected_output), 'Test failed'