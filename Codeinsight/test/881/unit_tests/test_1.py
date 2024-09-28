dict0 = {"Highlight": "yes", "HighFive": "no", "LowLight": "maybe"}
str0 = "High"
expected_result =  {"Highlight": "yes", "HighFive": "no"}
assert test(dict0, str0) == expected_result, 'Test failed'