def test(str0, lst0):
    slice_parts = {k: int(v) for k, v in enumerate(str0.split(':'))}
    return lst0[slice(slice_parts.get(0), slice_parts.get(1), slice_parts.get(2))]

