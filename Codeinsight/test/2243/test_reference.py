def test(trace_df):
    return (trace_df['ratio'] > 0).sum() / len(trace_df)

