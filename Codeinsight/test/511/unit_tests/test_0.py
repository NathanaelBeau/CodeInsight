lst0 = [{'date':'2012-01-01'}, {'date':'2011-01-03'}, {'date':'2012-02-02'}]
expected_result =  [{'date':'2011-01-03'}, {'date':'2012-01-01'}, {'date':'2012-02-02'}]
result = test(lst0)
assert result == expected_result, 'Test failed'