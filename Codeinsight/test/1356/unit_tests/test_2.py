html_str0 = "<div>First</div><div>Second</div>"
expected_result =  "First\nSecond"
result = test(html_str0)
assert result == expected_result, 'Test failed'