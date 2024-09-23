import pandas as pd 
import re

def test(df0, var0, str0, str1):
    df0[var0] = df0[var0].apply(lambda x: re.sub(str0, str1, x))
    return df0

