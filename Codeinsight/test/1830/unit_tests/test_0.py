str0 = '<a href="/blog/first">Link 1</a><a href="/blog/second">Link 2</a>'
regex_str = r'<a\s+href="/blog/(.+?)">'
expected_output= ('first', 'second')
assert test(str0, regex_str) ==expected_output, 'Test failed'