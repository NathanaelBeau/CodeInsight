arr0 = (10, 20, 30, 40, 50, 60, 70, 80)  
var0 = 2  
var1 = 4  
expected_output = np.array([[[10, 10, 10, 10],
                             [20, 20, 20, 20],
                             [30, 30, 30, 30],
                             [40, 40, 40, 40]],
                            [[50, 50, 50, 50],
                             [60, 60, 60, 60],
                             [70, 70, 70, 70],
                             [80, 80, 80, 80]]], dtype=np.uint8)  
reshaped_arr0 = np.array(arr0, dtype=np.uint8).reshape(var0, var1)
repeated_arr0 = np.repeat(reshaped_arr0[:, :, np.newaxis], 4, axis=2)
assert (repeated_arr0 == expected_output).all(), 'Test failed'