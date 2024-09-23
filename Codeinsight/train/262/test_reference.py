import pandas as pd
def test(df0, arg0):
    def filter_func(x):
        return x.endswith(arg0)

    return df0[df0.index.map(filter_func)]


