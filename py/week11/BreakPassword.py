"""BreakPassword"""
import hashlib
def main(password):
    """BreakPassword"""
    for i in range(0, 100000):
        passtest = "%05d"%i
        sha512 = hashlib.sha512(passtest.encode("UTF-8"))
        if sha512.hexdigest().upper() == password:
            print(passtest)
            break
main(input())
