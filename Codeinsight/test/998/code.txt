def test(lst0):
    idx = sorted(range(len(lst0)), key=lst0.__getitem__)
    ridx_dict = {k: v for v, k in enumerate(idx)}
    ridx = [ridx_dict[k] for k in range(len(idx))]
    return ridx