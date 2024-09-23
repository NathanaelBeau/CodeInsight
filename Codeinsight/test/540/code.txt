import pandas as pd
import numpy as np



def test(df0, var0):
    result_df = df0.groupby(var0).size().reset_index(name='count')
    result_df.set_index(var0, inplace=True)
    return result_df