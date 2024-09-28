arg = "OpenAI GPT-3"
expected_output = "b625c286c0c7646cd6c6b6c5af6c04aaf49db3ee414634df53c58b3df3f85804"
assert test(arg, 64) == expected_output, 'Test failed'