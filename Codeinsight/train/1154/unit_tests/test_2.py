class Obj:
    def __init__(self, modified):
        self.modified = modified
lst0_3 = [Obj(modified=1), Obj(modified=1), Obj(modified=1)]
var0_3 = "modified"
expected_output_3 = [Obj(modified=1), Obj(modified=1), Obj(modified=1)]
result_3 = test(lst0_3, var0_3)
assert all(x.modified == y.modified for x, y in zip(result_3, expected_output_3)), 'Test failed'