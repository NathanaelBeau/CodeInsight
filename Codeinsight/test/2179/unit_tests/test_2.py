lst0 = [["A", "B", "C"],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
expected_output = pd.DataFrame({"A": [1, 4, 7],
                                "B": [2, 5, 8],
                                "C": [3, 6, 9]})
assert test(lst0).equals(expected_output), 'Test failed'