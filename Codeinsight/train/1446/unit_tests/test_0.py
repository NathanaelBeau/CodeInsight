str0_test1 = "Hello world this is a sample sentence for testing."
var0_test1 = 25
expected_output_test1 = ["Hello world this is a", "sample sentence for", "testing."]
result_test1 = test(str0_test1, var0_test1)
assert result_test1 ==expected_output_test1, 'Test failed'