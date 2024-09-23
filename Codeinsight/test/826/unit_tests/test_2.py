byte_str = 'こんにちは'.encode('utf8')  # Japanese characters
result = test(byte_str)
expected = 'はちにんこ'.encode('utf8')
assert result ==expected, 'Test failed'