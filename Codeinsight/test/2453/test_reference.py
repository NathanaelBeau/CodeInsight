import numpy as np

def test(var0,data0, col0):
    order_array = np.array(var0, dtype=data0)
    order_array.sort(order=col0)
    return order_array

