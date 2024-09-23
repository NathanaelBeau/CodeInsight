def test(*lst_args):
    return list(map(sum, zip(*lst_args)))

