lst0 = [
            ('111', 'abc', 'def'),
            ('222', 'ghi', 'jkl'),
            ('333', 'mno', 'pqr'),
            ('111', 'stu', 'vwx'),
            ('222', 'yza', 'bcd')
        ]
expected_output = {'111': 2, '222': 2, '333': 1}
assert test(lst0) ==expected_output, 'Test failed'