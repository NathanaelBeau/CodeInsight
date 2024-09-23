# Create a sample DataFrame for testing
df_test = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Test the flattening function
result = test(df_test)
expected = [1, 4, 2,  5, 3, 6]

assert result.tolist() == expected, f"Test Failed"
