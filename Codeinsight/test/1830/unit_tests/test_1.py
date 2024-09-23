str0 = '<div>Content without any links</div>'
regex_str = r'<a\s+href="/blog/(.+?)">'
expected_output = ()
assert test(str0, regex_str) ==expected_output, 'Test failed'