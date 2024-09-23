dict0 = {"LightOne": 1, "DarkTwo": 2, "LightThree": 3, "LightFour": 4}
str0 = "Light"
expected_result =  {"LightOne": 1, "LightThree": 3, "LightFour": 4}
assert test(dict0, str0) == expected_result, 'Test failed'