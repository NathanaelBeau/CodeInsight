def test(lst0):
    set_ = set()
    for dict_ in lst0:
        set_.update(dict_.keys())
    return set_
