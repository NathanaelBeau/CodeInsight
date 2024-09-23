arg0 = '[,;.]'
arg1 = "Hello,world;this.is:a,test"
expected_output = ['Hello', 'world', 'this', 'is:a', 'test']
assert test(arg0, arg1) == expected_output, 'Test failed'