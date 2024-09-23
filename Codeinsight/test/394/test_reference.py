import binascii

def test(str0):
    try:
        hex_num = int(str0, 16)
        return hex_num
    except ValueError:
        return None
