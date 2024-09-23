str0 = "This is another #example with an #accentué character"
expected_output = ["example", "accentué"]
assert test(str0) ==expected_output, 'Test failed'