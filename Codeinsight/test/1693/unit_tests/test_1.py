s2 = "Split@Here!And?Here."
expected_output2 = ['Split', '@', 'Here', '!', 'And', '?', 'Here', '.']
assert test(s2) == expected_output2, 'Test failed'