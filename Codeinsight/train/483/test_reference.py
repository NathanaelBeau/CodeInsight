import pandas as pd
import re

def test(df0, column_name, lst0):
    escaped_lst0 = [re.escape(substring) for substring in lst0]
    return df0[column_name].str.contains('|'.join(escaped_lst0))

