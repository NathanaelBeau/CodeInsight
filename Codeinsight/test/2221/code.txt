from email.headerregistry import Address

def test(str0):
    return Address(addr_spec=str0).username
