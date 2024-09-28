lst0 = ['apple_for_banana', 'orange_and_grape', 'mango_or_peach']
expected_output = [['apple', 'banana'], ['orange', 'grape'], ['mango', 'peach']]
assert test(lst0) ==expected_output, 'Test failed'