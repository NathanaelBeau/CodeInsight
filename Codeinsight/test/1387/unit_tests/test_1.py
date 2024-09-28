str0 = "   Leading and trailing spaces   "
expected_result =  "Leadingandtrailingspaces"
result = test(str0)
assert result == expected_result, 'Test failed'