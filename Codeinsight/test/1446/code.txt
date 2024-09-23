import collections

def test(dict0):
    sorted_dict = collections.OrderedDict(sorted(dict0.items()))
    return sorted_dict
