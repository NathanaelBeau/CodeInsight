import struct

def test(str0):
    format_string = f"{len(str0)//2}B"  # Adjust the format string based on half of the input length
    byte_values = struct.unpack(format_string, bytes.fromhex(str0))
    return list(byte_values)