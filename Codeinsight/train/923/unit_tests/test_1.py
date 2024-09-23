lst0 = [{'date':'2022-05-01'}, {'date':'2021-03-03'}, {'date':'2023-04-02'}]
expected_result =  [{'date':'2021-03-03'}, {'date':'2022-05-01'}, {'date':'2023-04-02'}]
result = test(lst0)
assert result == expected_result, 'Test failed'