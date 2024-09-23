str0 = "color-red,shape-circle,size-large"
expected_result =  {'color': 'red', 'shape': 'circle', 'size': 'large'}
result = test(str0)
assert result == expected_result, 'Test failed'