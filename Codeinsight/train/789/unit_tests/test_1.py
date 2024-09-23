dt1 = datetime(2022, 1, 1, 12, 0, 0)
days1 = 1
hours1 = 3
expected_result =  dt1 + timedelta(days=1, hours=3)
result = test(dt1, days1, hours1)
assert result == expected_result, 'Test failed'