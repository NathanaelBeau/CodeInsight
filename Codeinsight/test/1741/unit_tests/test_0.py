str0 = "This is a #test text with #hashtags"
expected_output = ["test", "hashtags"]
assert test(str0) ==expected_output, 'Test failed'