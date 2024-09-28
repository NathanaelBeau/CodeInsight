tensor0 = torch.tensor([1, 2, 3, 4, 5, 6])
shape0 = (2, 3)
expected_result =  torch.tensor([[1, 2, 3], [4, 5, 6]])
result = test(tensor0, shape0)
assert torch.equal(result, expected_result), 'Test failed'