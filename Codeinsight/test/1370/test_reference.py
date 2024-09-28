def test(df0, str0, var1, str1):
    # Split the specified column and expand into new columns
    split_columns = df0[str0].str.split(var1, expand=True)
    
    # Create a new DataFrame with the split columns
    split_df = pd.DataFrame(split_columns)

    # Concatenate the split columns back to the original DataFrame, dropping the original column
    df_expanded = pd.concat([df0.drop(columns=[str0]), split_df], axis=1)
    
    # Reorder the columns as specified by str1
    return df_expanded[str1]