"""GraderMachine"""
def main():
    """GraderMachine"""
    start = int(input())
    end = int(input())
    word = ""
    result = 0
    for _ in range(abs(start-end)+1):
        if start <= end:
            if start%2 == 0:
                word = word+str(start)+" "
                result += start
                start += 1
            else:
                start += 1
        elif start > end:
            if start%2 == 0:
                word = word+str(start)+" "
                result += start
                start -= 1
            else:
                start -= 1
    print("pass : "+word)
    print("Sum : %d"%result)

main()
