import numpy as np

def test(arr0, var0, var1):
    reshaped_arr0 = np.array(arr0, dtype=np.uint8).reshape(var0, var1)

    repeated_arr0 = np.repeat(reshaped_arr0[:, :, np.newaxis], 4, axis=2)

    expected_output = repeated_arr0  
    return np.array_equal(repeated_arr0, expected_output)

