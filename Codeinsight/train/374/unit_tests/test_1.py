expected_columns = ['A', 'B', 'A1R', 'B2', 'AABB4']
assert test().columns.tolist() == expected_columns, 'Test failed'