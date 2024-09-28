str0 = "This Is A Test String With No Capitalized Words."
expected_output = ['This', 'Is', 'A', 'Test', 'String', 'With', 'No', 'Capitalized', 'Words.']
assert test(str0) ==expected_output, 'Test failed'