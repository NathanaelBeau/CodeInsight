html_str0 = "<p>Hello!</p><br><p>World!</p>"
expected_result =  "Hello!\nWorld!"
result = test(html_str0)
assert result == expected_result, 'Test failed'