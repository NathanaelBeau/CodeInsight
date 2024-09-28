import pandas as pd
import numpy as np
def test(df):
    return df.groupby('Event')['Status'].value_counts().unstack().fillna(0)
