lst0 = [['C'], ['B'], ['A'], ['C', 'B'], ['B', 'A'], ['A', 'C']]
expected_output = [['A'], ['B'], ['C'], ['A', 'B'], ['A', 'C'], ['B', 'C']]
assert test(lst0) ==expected_output, 'Test failed'