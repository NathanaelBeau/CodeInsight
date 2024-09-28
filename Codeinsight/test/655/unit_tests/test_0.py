lst0 = [['a', 'b'], ['c'], ['d', 'e'], ['f', 'g'], ['h']]
expected_output = [
    ('a', 'c', 'd', 'f', 'h'),
    ('a', 'c', 'd', 'g', 'h'),
    ('a', 'c', 'e', 'f', 'h'),
    ('a', 'c', 'e', 'g', 'h'),
    ('b', 'c', 'd', 'f', 'h'),
    ('b', 'c', 'd', 'g', 'h'),
    ('b', 'c', 'e', 'f', 'h'),
    ('b', 'c', 'e', 'g', 'h')
]
assert expected_output == list(itertools.product(*lst0)), 'Test failed'