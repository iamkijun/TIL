import sys
sys.stdin = open("Greedy/input.txt","r")

n = int(input())

cnt = 0

while True:
    if n == -1:
        cnt= -1
        break
    
    elif n == 0:
        break

    elif n % 5 == 0:
        cnt += n//5
        break

    else:
        n -= 2
        cnt += 1

print(cnt)
