lst0 = [{'name': 'John', 'info': {'age': 30, 'country': 'USA'}}, {'name': 'Jane', 'info': {'age': 25, 'country': 'UK'}}]
expected_result =  pd.DataFrame({'name': ['John', 'Jane'], 'info.age': [30, 25], 'info.country': ['USA', 'UK']})
assert test(lst0).equals(expected_result), 'Test failed'