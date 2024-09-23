from itertools import islice

def test(lst0, window_size=2):
    it = iter(lst0)
    result = tuple(islice(it, window_size))
    moving_averages = []

    if len(result) == window_size:
        moving_averages.append(sum(result) / window_size)
        
    for elem in it:
        result = result[1:] + (elem,)
        moving_averages.append(sum(result) / window_size)

    return moving_averages
