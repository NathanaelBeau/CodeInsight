import urllib.parse

def test(var0):
    original_string = var0
    url_encoded = urllib.parse.quote(original_string.encode('utf8'))
    decoded_bytes = urllib.parse.unquote_to_bytes(url_encoded)
    decoded_string = decoded_bytes.decode('utf8')
    return decoded_string


