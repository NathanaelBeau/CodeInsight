import collections.abc

def test(str0, str1):
    matching = [el for el in str0 if isinstance(el, collections.abc.Iterable) and (str1 in el)]
    return matching
