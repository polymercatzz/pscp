"""Safe"""
def main(pass1, pass2):
    """Safe"""
    result = 0
    for i, _ in enumerate(pass1):
        mak = max(ord(pass1[i]), ord(pass2[i]))
        noi = min(ord(pass1[i]), ord(pass2[i]))
        result += min(abs(mak-noi), (90-mak+noi)%64)
    print(result)
main(input(), input())
