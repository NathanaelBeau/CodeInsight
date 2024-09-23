def test(lst0, var0):
    segment_length = len(lst0) // var0
    return [lst0[i:i + segment_length] for i in range(0, len(lst0), segment_length)]