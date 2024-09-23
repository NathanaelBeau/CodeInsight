var0 = "prefixSome text here.suffix"
pattern = r"(?<=prefix).*(?=suffix)"
expected_output1 = "Some text here."
assert test(var0, pattern) == expected_output1, 'Test failed'