def test(*lst_args):
    return [sum(x) for x in zip(*lst_args)]

