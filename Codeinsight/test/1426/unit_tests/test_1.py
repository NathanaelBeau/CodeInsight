arr0 = (15, 25, 35, 45, 55, 65, 75, 85)
var0 = 2
var1 = 4
expected_output = np.array([[[15, 15, 15, 15],
                                   [25, 25, 25, 25],
                                   [35, 35, 35, 35],
                                   [45, 45, 45, 45]],
                                  [[55, 55, 55, 55],
                                   [65, 65, 65, 65],
                                   [75, 75, 75, 75],
                                   [85, 85, 85, 85]]], dtype=np.uint8)
reshaped_arr0 = np.array(arr0, dtype=np.uint8).reshape(var0, var1)
repeated_arr0 = np.repeat(reshaped_arr0[:, :, np.newaxis], 4, axis=2)
assert (repeated_arr0 == expected_output).all(), 'Test failed'