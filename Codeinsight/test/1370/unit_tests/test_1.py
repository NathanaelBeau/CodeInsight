str0 = "Hello world, hello universe"
var0 = "hello"
var1 = "hi"
bool0 = False
result = test(str0, var0, var1, bool0)
expected = "Hello world, hi universe"
assert result == expected, 'Test failed'