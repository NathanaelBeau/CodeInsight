from bs4 import BeautifulSoup

def test(str0):
    soup = BeautifulSoup(str0, 'html.parser')
    return soup.get_text('\n')
