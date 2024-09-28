expected_result =  pd.DataFrame(columns=['A', 'B', 'A1R', 'B2', 'AABB4'])
assert test().equals(expected_result), 'Test failed'