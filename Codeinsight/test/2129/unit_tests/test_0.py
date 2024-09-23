var0 = r'(<textarea.*>).*(</textarea>)'
var1 = r'\1Bar\2'
str0 = "<textarea>This is a sample text</textarea>"
expected_output = "<textarea>Bar</textarea>"
assert test(var0, var1, str0) ==expected_output, 'Test failed'