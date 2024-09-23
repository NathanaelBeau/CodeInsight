import urllib.parse

def test(var0):
    original_string = var0
    url_encoded = urllib.parse.quote(original_string.encode('utf8'))
    decoded_string = urllib.parse.unquote(url_encoded)
    return decoded_string

