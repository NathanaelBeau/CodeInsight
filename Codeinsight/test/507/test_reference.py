from ast import literal_eval

def test(str0):
    float_str = str0.replace("-0b", "-0b0")
    result = float(literal_eval(float_str))
    return result

