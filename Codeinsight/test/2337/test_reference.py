def test(trace_df):
    return len(trace_df[trace_df['ratio'] > 0]) / len(trace_df)

