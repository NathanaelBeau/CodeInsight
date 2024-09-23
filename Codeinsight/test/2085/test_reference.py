import numpy as np
def test(rows=1, columns=['A']):
    if rows == 0:
        return pd.DataFrame(columns=columns)
    return pd.DataFrame(np.nan, index=range(rows), columns=columns)

