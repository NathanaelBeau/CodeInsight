dict0 = {"SomeLight": "on", "NoLightHere": "off", "TotallyDark": "absent"}
str0 = "Dark"
expected_result =  {"TotallyDark": "absent"}
assert test(dict0, str0) == expected_result, 'Test failed'