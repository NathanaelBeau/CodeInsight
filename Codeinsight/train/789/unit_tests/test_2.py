dt0 = datetime(2020, 6, 15, 8, 30, 0)
days0 = 2
hours0 = 5
expected_result =  dt0 + timedelta(days=2, hours=5)
result = test(dt0, days0, hours0)
assert result == expected_result, 'Test failed'