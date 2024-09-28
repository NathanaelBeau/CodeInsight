from datetime import datetime

def test(str0):
    return datetime.strptime(str0, "%Y-%m-%d %H:%M:%S.%f")
