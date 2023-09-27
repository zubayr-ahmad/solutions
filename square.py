import math as ma
def findSquare(n,m,a):
    return ma.ceil(n/a) * ma.ceil(m/a)

var = list(map(int,input().split()))
print(findSquare(var[0],var[1],var[2]))





