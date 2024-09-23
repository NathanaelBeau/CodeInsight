lst0=['key1', 'value1', 'key2']
expected_output = [('key2', 'value1', 'key1'), ('key2', 'key1', 'value1'), ('value1', 'key2', 'key1'), ('value1', 'key1', 'key2'), ('key1', 'key2', 'value1'), ('key1', 'value1', 'key2')]
assert all(elem in test(lst0) for elem in expected_output), 'Test failed'