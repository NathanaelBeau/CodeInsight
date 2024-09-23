from datetime import date
expected_result =  date.today().strftime("%Y-%m-%d")
result = test()
assert result == expected_result, 'Test failed'