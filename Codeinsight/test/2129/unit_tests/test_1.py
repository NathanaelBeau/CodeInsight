var0 = r'(http|https)://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?'
var1 = r'URL'
str0 = "Visit my website at http://www.example.com"
expected_output = "Visit my website at URL"
assert test(var0, var1, str0) ==expected_output, 'Test failed'