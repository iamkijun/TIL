import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1,T+1):
    N = int(input())
    li = [2,3,5,7,11]
    count = [0] * 5

    for val in li:
        tem_N = N
        while True:
            if tem_N % val == 0:
                count[li.index(val)] +=1
                tem_N = tem_N // val
            elif tem_N % val != 0:
                break

    print(f'#{i}', *count)