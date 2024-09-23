import re

def test(str0):
    def only_numerics(seq):
        seq_type = type(seq)
        return seq_type().join(filter(seq_type.isdigit, seq))
    
    return only_numerics(str0)

