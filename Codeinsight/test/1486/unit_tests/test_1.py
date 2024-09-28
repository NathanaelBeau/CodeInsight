dct0 = {"x": 10, "y": 20, "z": 30}
dct1 = {"w": 40, "x": 50, "y": 60}
expected_result =  {"x": 10, "y": 20}
result = test(dct0, dct1)
assert result == expected_result, 'Test failed'