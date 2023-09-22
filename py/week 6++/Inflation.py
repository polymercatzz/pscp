"""Inflation"""
def main():
    '''Inflation'''
    numn = float(input())
    numk = int(input())
    numn = int(numn*100)
    for _ in range(numk):
        numn += ((numn*381)//10000)
    print('%d.%02d'%((numn//100), numn%100))
main()
