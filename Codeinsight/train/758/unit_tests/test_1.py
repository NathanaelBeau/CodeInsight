from bs4 import BeautifulSoup
html_content = """
<html>
    <body>
        <a href="#">Elsie</a>
        <a href="#">Lacie</a>
        <a href="#">Tillie</a>
        <a href="#">Elsie</a>
    </body>
</html>
"""
soup = BeautifulSoup(html_content, 'html.parser')
soup0 = soup
str0 = 'Lacie'
expected_result =  [tag for tag in soup.find_all('a') if tag.string == 'Lacie']
result = test(soup0, str0)
assert result == expected_result, 'Test failed'