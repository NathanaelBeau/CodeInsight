def test(str0):
    try:
        
        str0 = str0.strip().lstrip("0x").lstrip("0X")
        
        
        hex_num = int(str0, 16)
        return hex_num
    except ValueError:
        return None
