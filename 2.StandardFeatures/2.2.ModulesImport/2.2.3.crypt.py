from simplecrypt import encrypt, decrypt, DecryptionException


def read_passwords():
    with open('passwords.txt', 'r') as passwords_file:
        passwords = map(str.strip, passwords_file.readlines())
    return passwords


def test():
    with open("encrypted.bin", "rb") as inp:
        encrypted = inp.read()

    for password in read_passwords():
        try:
            print(decrypt(password, encrypted))
        except DecryptionException:
            print('{} is a  bad password'.format(password))


test()
