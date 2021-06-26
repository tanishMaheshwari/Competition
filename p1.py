from fractions import Fraction-
def getHcf(x, y):
    for i in range(1, max(x, y)+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf



def getLcm(x, y):
    return x * y // math.gcd(x, y)

def sumOfDigits(inputList):
    for i in range(len(inputList)):
        n = inputList[i]
        num, den = [], []
        
        for j in range(1, n + 1):
            num.append(j)
            den.append(n**2 + j)
        
        #hcf of denominators
        lcm = 1
        for k in range(len(den)):
            lcm = den[k] * lcm // math.gcd(lcm, den[k])
        finalNum = 0
        #Getting numerAator for final fraction
        for i in range(len(num)):
            finalNum += num[i] * int(lcm / den[i])
        
        
        #Simplufuing the fraction
        while True:
            hcf = math.gcd(lcm, finalNum) 
            if hcf != 1:
                lcm = int(lcm / hcf)
                finalNum = int(finalNum / hcf)
            else:
                print(finalNum + lcm)
                break


if __name__ == "__main__":
    a = int(input())
    inputList = [] 
    for i in range(a):
        inputList.append(int(input()))

    sumOfDigits(inputList)
        
