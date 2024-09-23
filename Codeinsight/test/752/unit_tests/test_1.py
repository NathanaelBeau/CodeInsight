lst0 = [["Name", "Age", "City"],
        ["Alice", 25, "New York"],
        ["Bob", 30, "Los Angeles"],
        ["Charlie", 22, "Chicago"]]
expected_output = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"],
                                "Age": [25, 30, 22],
                                "City": ["New York", "Los Angeles", "Chicago"]})
assert test(lst0).equals(expected_output), 'Test failed'