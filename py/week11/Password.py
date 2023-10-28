"""Password"""
import hashlib
def main(password):
    """Password"""
    sha512 = hashlib.sha512(password.encode("UTF-8"))
    print(sha512.hexdigest().upper())
main(input())
