def test(str0):
    return {x.split('=')[0]: x.split('=')[1] for x in str0.split()}

