import pandas as pd
from itertools import chain

def test(lst0):
    df = pd.DataFrame(lst0)
    categories_list = list(chain(*df['categories'].values.tolist()))
    value_counts = pd.value_counts(categories_list).to_dict()
    return value_counts