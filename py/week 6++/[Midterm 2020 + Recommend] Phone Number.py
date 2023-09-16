"""[Midterm 2020 + Recommend] Phone Number"""
def main():
    """[Midterm 2020 + Recommend] Phone Number"""
    phone = input()
    word = input()
    if word == "International":
        phone = "+66"+ phone[1:]
    print(phone[:-8]+" "+phone[-8:-4]+" "+phone[-4:])
main()
