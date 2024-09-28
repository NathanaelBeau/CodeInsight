lst0 = [
        {'id': 1, 'title': 'Python Programming', 'duration': 60},
        {'id': 2, 'title': 'Data Science', 'duration': 120},
        {'id': 3, 'title': 'Machine Learning', 'duration': 180},
        {'id': 4, 'title': 'Deep Learning', 'duration': 240},
    ]
expected_output = {'id', 'title', 'duration'}
assert test(lst0) ==expected_output, 'Test failed'