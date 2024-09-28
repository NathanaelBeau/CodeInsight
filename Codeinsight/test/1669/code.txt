import pandas as pd

def test(nvalues: dict) -> pd.DataFrame:
    return pd.DataFrame.from_dict(nvalues)

