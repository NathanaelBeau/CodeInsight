tensor0 = torch.tensor([10, 20, 30, 40, 50, 60])
shape0 = (3, 2)
expected_result =  torch.tensor([[10, 20], [30, 40], [50, 60]])
result = test(tensor0, shape0)
assert torch.equal(result, expected_result), 'Test failed'