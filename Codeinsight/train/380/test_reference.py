def test(lst0):
    return sum(d['gold'] for d in lst0 if 'gold' in d)

