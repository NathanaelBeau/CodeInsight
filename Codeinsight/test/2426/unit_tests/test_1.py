str0 = "hello.world.this.is.a.test"
str1 = "."
expected_result =  ["hello.world.this.is.a", "test"]
result = test(str0, str1)
assert result == expected_result, 'Test failed'