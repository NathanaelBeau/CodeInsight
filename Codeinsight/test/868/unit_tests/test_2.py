str0 = '<a href="/blog/first">Link 1</a>'
regex_str = r'<a\s+href="/blog/(.+?)">'
expected_output = ('first',)
assert test(str0, regex_str) ==expected_output, 'Test failed'