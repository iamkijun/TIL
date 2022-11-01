import sys
sys.stdin = open('Math/input.txt','r')

N = int(input())

def prime_num(N):
    if N == 1:
        return False
    
    for i in range(2,int(N**0.5)+1):
        if N % i == 0:
            return False
    else:
        return True
        

def palindrome(N):
    str_N = str(N)

    if str_N == str_N[::-1]:
        return True

    return False

while True:
    if prime_num(N) and palindrome(N):
        print(N)
        break
    else:
        N += 1
    
# print(prime_num(101))