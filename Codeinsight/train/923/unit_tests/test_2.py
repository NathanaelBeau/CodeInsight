lst0 = [{'date':'2010-07-04'}, {'date':'2009-08-15'}, {'date':'2011-09-06'}]
expected_result =  [{'date':'2009-08-15'}, {'date':'2010-07-04'}, {'date':'2011-09-06'}]
result = test(lst0)
assert result == expected_result, 'Test failed'