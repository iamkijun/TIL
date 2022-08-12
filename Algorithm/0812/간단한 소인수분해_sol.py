import sys
sys.stdin = open("input.txt","r")

    T = int(input())

    for t in range(1, T+1):

        divs = [2,3,5,7,11]
        cnts = [0,0,0,0,0]

        n = int(input())

        for i in range(5):
            while True:
                if n % divs[i] == 0:
                    cnts[i] += 1
                    n= n//divs[i]
                else:
                    break

        print(f'#{t} ',*cnts)