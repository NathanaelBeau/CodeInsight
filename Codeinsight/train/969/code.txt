import pandas as pd
import re

def test(df0, column_name, lst0):
    result = pd.Series([False] * len(df0))
    for substring in lst0:
        result |= df0[column_name].str.contains(re.escape(substring))
    return result
