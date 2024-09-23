result = test("No match here!", "pattern", "replacement", False)
expected = "No match here!"
assert result == expected, 'Test failed'