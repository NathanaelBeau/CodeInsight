import pandas as pd
def test(lst0):
    return pd.DataFrame.from_records([obj.to_dict() for obj in lst0])
