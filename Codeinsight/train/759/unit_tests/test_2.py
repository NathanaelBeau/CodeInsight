lst0 = []
lst1 = []
expected_result =  pd.DataFrame({'List1': [], 'List2': []}).reset_index(drop=True)
result = test(lst0, lst1).reset_index(drop=True)
assert result.empty, 'Test failed'