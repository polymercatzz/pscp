"""AlmostMean"""
def main():
    """AlmostMean"""
    num = int(input())
    people = []
    lis_score = []
    average = 0
    for _ in range(num):
        people += list(input().split("	"))
    for score in people[1::2]:
        average += float(score)
    average /= num
    for score in people[1::2]:
        if float(score) <= average:
            lis_score.append(float(score))
    lis_score.sort()
    most_score = str(lis_score[-1])
    print("%s	%s"%(people[people.index(most_score)-1], most_score))
main()
