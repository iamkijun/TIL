import sys
sys.stdin = open('DP/input.txt','r')

N = int(input())

cnt= 0 

def sugar(n):
    global cnt
    
    while True:
        if n % 5 == 0:
            cnt += n//5
            break
        
        else:
            if n<=2:
                cnt = -1
                break
            n -= 3
            cnt += 1
    
    return cnt

print(sugar(N))