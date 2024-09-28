var0 = r'abc(de)fg(123)'
str0 = 'abcdefg123 and again abcdefg123'
expected_output = [('de', '123'), ('de', '123')]
assert test(var0, str0) ==expected_output, 'Test failed'