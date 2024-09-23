lst0 = [{'name': 'Sarah', 'language': 'Python'},
        {'name': 'Michael', 'language': 'Java'},
        {'name': 'Linda', 'language': 'C++'}]
var0 = 'name'
expected_output = {'Sarah': {'language': 'Python'},
                   'Michael': {'language': 'Java'},
                   'Linda': {'language': 'C++'}}
assert test(lst0, var0) == expected_output, 'Test failed'