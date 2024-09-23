lst2 = [{'file_name': 'docM', 'file_number': 40},
        {'file_name': 'docN', 'file_number': 20},
        {'file_name': 'docO', 'file_number': 30}]
expected_result2 = [{'file_name': 'docN', 'file_number': 20},
                    {'file_name': 'docO', 'file_number': 30},
                    {'file_name': 'docM', 'file_number': 40}]
result2 = test(lst2, 'file_number')
assert result2 == expected_result2, 'Test failed'