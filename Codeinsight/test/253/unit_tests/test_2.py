lst0 = [100, 200, 300]
lst1 = [[400], [500], [600]]
expected_output = [[100, 400], [200, 500], [300, 600]]
assert test(lst0, lst1) ==expected_output, 'Test failed'