str0 = "This is a test string with z's"
var0= "z"
var1= "s"
expected_output = ['Thi', ' i', ' a te', 't ', 'tring with ', "'", '']
assert test(str0, var0, var1) ==expected_output, 'Test failed'