import numpy as np
def test(rows=1, columns=['A']):
    return pd.DataFrame(index=range(rows), columns=columns, dtype=float)
