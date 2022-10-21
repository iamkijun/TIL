import sys
# input = sys.stdin.readline
sys.stdin = open('Brute_Force/input.txt','r')

A = int(input())

T = int(input())

bdg = int(input())

def finding():
    n = 2 #현재 반복 횟수
    cnt = 0
    total = 0

    while True:
        bdg_li = [0,1,0,1]+ [0]*n + [1]*n
        cnt += len(bdg_li)//2

        if cnt >= T:
            
            cnt -= len(bdg_li)//2

            for val in bdg_li:

                total+=1

                if val == bdg:
                    cnt+=1

                    if cnt == T:
                        return total

        else:
            n+=1
            total += len(bdg_li)

print((finding()-1)%A)