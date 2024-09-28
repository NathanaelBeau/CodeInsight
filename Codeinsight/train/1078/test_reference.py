import pandas as pd

def test(df0, var0):
    total_count = 0
    positive_count = 0

    for value in df0[var0]:
        total_count += 1
        if value > 0:
            positive_count += 1

    return positive_count / total_count