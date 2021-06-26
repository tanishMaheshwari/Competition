from fractions import Fraction
import math
def sumOfDigits(inputList):
    for i in range(len(inputList)):
        n = inputList[i]
        x = 0
        for j in range(1, n + 1):
            x += Fraction(j, (n *n) + j)
        if x == 0:
            print(3)
        else:
            a = str(x).split('/')
            x, y = int(a[0]), int(a[1])    
            while True:
                if math.gcd(x, y) != 1:
                    x, y = int(x / math.gcd(x, y)), int(y / math.gcd(x, y))
                else:
                    _ = list(str(x+y))
                    s = 0
                    
                    for l in range(len(_)):
                        s +=  int(_[l]) 
                    print(s)
                    break


if __name__ == "__main__":
    a = int(input())
    inputList = [] 
    for i in range(a):
        inputList.append(int(input()))

    sumOfDigits(inputList)
        
