import pandas

def test(var0, var1):
    df = var0
    df[df.columns[0]] = df[df.columns[0]].map(lambda a: var1(a))
    return df