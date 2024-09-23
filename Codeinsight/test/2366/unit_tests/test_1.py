str0 = 'x;y;z;d'
str1= ";"
str2= ":"
var0 = 0
var1 = 3
expected_output = 'x:y:z;d'
assert test(str0, var0, var1, str1, str2) ==expected_output, 'Test failed'