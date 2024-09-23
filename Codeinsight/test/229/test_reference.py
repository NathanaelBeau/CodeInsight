import pandas as pd
def test(lst0):
    df = pd.DataFrame(lst0)
    stacked = df['categories'].explode()
    value_counts = stacked.value_counts().to_dict()
    return value_counts