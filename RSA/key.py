from Crypto.PublicKey import RSA

def write_to_file(key, filename):
    with open(filename, "w") as file:
        file.write(key.decode())

def read_to_file(filename):
    with open(filename, "r") as file:
        key = file.read()
        return key

def print_public_key():
    public_key = read_to_file('public_key.pem')
    print(public_key)

def print_private_key():
    private_key = read_to_file('private_key.pem')
    print(private_key)

private_key, public_key = read_to_file('private_key.pem'), read_to_file('public_key.pem')     