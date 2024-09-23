def test(df0, col_name, lst0):
    query_str = f"{col_name} in @lst0"
    return df0.query(query_str)
