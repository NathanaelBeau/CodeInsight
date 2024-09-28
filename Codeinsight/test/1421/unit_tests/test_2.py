lst0 = []
lst1 = []
expected_result =  pd.DataFrame({'List1': [], 'List2': []})
result = test(lst0, lst1)
assert result.empty, 'Test failed'