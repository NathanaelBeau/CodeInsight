lst0 = [10, 20, 30, 40, 50, 60, 70]
window_size = 3
expected_output = [20.0, 30.0, 40.0, 50.0, 60.0] 
assert test(lst0, window_size) ==expected_output, 'Test failed'