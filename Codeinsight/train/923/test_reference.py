from datetime import datetime

def test(lst0):
    return sorted(lst0, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d"))

