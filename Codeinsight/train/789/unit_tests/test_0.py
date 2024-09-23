dt0 = datetime.now()
days0 = 1
hours0 = 3
expected_result =  dt0 + timedelta(days=1, hours=3)
result = test(dt0, days0, hours0)
assert result == expected_result, 'Test failed'