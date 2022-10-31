import sys
sys.stdin = open("input.txt","r")

T = int(input())

tbl = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dict ={tbl[n]: n for n in range(10)}

for t in range(1, T+1):
    _, N = map(str, input().split())
    N = int(N)
    li = list(input().split())

    # [1] 받은 숫자 자리를 누적
    counts = [0]*10
    for st in li:
        counts[dict[st]] += 1

    # [2] sols 결과의 개수만큼 str 붙이기
    sols = []
    for i in range(10):
        sols.append((tbl[i]+' ') * counts[i])

    print(f'#{t}')
    print(*sols)


