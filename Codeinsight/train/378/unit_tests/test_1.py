str0 = "Num"
lst0 = ["1", "2", "3"]
expected_result =  ["Num1", "Num2", "Num3"]
result = test(str0, lst0)
assert result == expected_result, 'Test failed'