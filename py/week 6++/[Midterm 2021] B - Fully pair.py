"""[Midterm 2021] B - Fully pair?"""
def main(word):
    """[Midterm 2021] B - Fully pair?"""
    result = ""
    for i in word:
        if i not in result:
            if word.count(i)%2 == 1:
                result += i
    if result == "":
        print("fully paired")
    else:
        print(result)
main(input())
