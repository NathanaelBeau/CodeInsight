str0 = "Convert [this] [string] into [nested] [lists]"
expected_output = [['this'], ['string'], ['nested'], ['lists']]
assert test(str0) == expected_output, 'Test failed'