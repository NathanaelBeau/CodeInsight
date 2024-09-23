from datetime import date
def test():
    today = date.today()
    return today.strftime("%Y-%m-%d")

