lst0 = [
            ('12392', 'some string', 'some other string'),
            ('12392', 'some new string', 'some other string'),
            ('7862', None, 'some other string')
        ]
expected_output = {'12392': 2, '7862': 1}
assert test(lst0) ==expected_output, 'Test failed'