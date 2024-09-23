def test(lst0):
    return [d for d in lst0 if d.get('language') == 'en'] + [d for d in lst0 if d.get('language') != 'en']


