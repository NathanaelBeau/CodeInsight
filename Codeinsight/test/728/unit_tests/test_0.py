lst0 = [{'file_name': 'docA', 'file_number': 3},
        {'file_name': 'docB', 'file_number': 1},
        {'file_name': 'docC', 'file_number': 2}]
expected_result =  [{'file_name': 'docB', 'file_number': 1},
                   {'file_name': 'docC', 'file_number': 2},
                   {'file_name': 'docA', 'file_number': 3}]
result = test(lst0, 'file_number')
assert result == expected_result, 'Test failed'