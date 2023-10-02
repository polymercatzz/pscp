"""AlmostMean"""
def main(num):
    """AlmostMean"""
    people = []
    lis_score = []
    average = 0
    for _ in range(num):
        people.extend(input().split("	"))
    for score in people[1::2]:
        average += float(score)/num
    for score in people[1::2]:
        if float(score) <= average:
            lis_score.append(float(score))
    lis_score.sort()
    print("%s	%s"%(people[people.index(str(lis_score[-1]))-1], lis_score[-1]))
main(int(input()))
