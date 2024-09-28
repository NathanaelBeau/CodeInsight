lst0 = [["Sequence", "Start", "End", "Coverage"],
        ["A", 1, 10, 0.95],
        ["B", 15, 25, 0.80],
        ["C", 30, 40, 0.60]]
expected_output = pd.DataFrame({"Sequence": ["A", "B", "C"],
                                "Start": [1, 15, 30],
                                "End": [10, 25, 40],
                                "Coverage": [0.95, 0.80, 0.60]})
assert test(lst0).equals(expected_output), 'Test failed'