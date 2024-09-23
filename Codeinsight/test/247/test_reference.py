import numpy as np

def test(var0, slice_rows, slice_cols, extend_rows, extend_cols):
    sliced = var0[slice_rows, slice_cols]
    if extend_rows is not None:
        sliced = np.vstack([sliced, extend_rows])
    if extend_cols is not None:
        sliced = np.hstack([sliced, extend_cols])
    return sliced