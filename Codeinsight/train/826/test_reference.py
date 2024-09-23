import pandas as pd
def test(var0):
    return var0.groupby('variable').size().reset_index(name='counts')

