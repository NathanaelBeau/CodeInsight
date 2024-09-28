from itertools import islice

def test(lst0, window_size=2):
    moving_averages = []
    window_sum = sum(lst0[:window_size])
    moving_averages.append(window_sum / window_size)

    for i in range(window_size, len(lst0)):
        window_sum = window_sum - lst0[i - window_size] + lst0[i]
        moving_averages.append(window_sum / window_size)

    return moving_averages