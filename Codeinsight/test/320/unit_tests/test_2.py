lst0 = [("USA", 10), ("China", 20), ("Russia", 10), ("Japan", 5), ("France", 10)]
expected_output = [("China", 20), ("France", 10), ("Russia", 10), ("USA", 10), ("Japan", 5)]
assert test(lst0) ==expected_output, 'Test failed'