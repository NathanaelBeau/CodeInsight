def test(str0):
    dict0 = dict((k.strip(), v.strip()) for k,v in (item.split('-') for item in str0.split(',')))
    return dict0
