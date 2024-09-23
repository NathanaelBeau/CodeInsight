lst1 = [{'file_name': 'docX', 'file_number': 10},
        {'file_name': 'docY', 'file_number': 5},
        {'file_name': 'docZ', 'file_number': 8}]
expected_result1 = [{'file_name': 'docY', 'file_number': 5},
                    {'file_name': 'docZ', 'file_number': 8},
                    {'file_name': 'docX', 'file_number': 10}]
result1 = test(lst1, 'file_number')
assert result1 == expected_result1, 'Test failed'