import pandas as pd
import numpy as np

def test(df0, var0):
    grouped = df0.groupby(var0)
    result_df = grouped.size().to_frame(name='count')  
    return result_df
