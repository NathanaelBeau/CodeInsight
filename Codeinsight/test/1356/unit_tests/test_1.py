html_str0 = "<h1>Title</h1><br><p>Some content.</p>"
expected_result =  "Title\nSome content."
result = test(html_str0)
assert result == expected_result, 'Test failed'