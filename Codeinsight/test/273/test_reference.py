import struct

def test(str0):
    int_value = int(str0, 2)
    bf = int_value.to_bytes((int_value.bit_length() + 7) // 8, byteorder='big', signed=False)
    return struct.unpack('>d', bf)[0]
