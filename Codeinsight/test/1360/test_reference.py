import pandas as pd

def test(lst0):
    df = pd.DataFrame(lst0)
    stacked = df['categories'].apply(tuple).explode()
    value_counts = stacked.value_counts()
    return value_counts.to_dict()