import sys
sys.stdin = open("input.txt", "r", encoding="UTF8")
def BruteForce(st,N,p,M,i):
    for j in range(M):
        if st[i+j] != p[j]:
            return False
    return True


for t in range(1,11):
    # 브루트 포스로 푼 방식 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    kijun = int(input())
    p = input()
    st = input()
    N = len(st)
    M = len(p)
    ans = 0

    for i in range(N-M+1):
        if BruteForce(st,N,p,M,i):
            ans +=1



    print(f'#{t} {ans}')
    # 직접 푼 방식>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # N = int(input())
    #
    # find_word = list(map(str,input()))
    #
    # s = list(map(str,input()))
    #
    # count = 0
    #
    # for i in range(len(s)-len(find_word)):
    #     if s[i:i+len(find_word)] == find_word:
    #         count+=1
    #
    #
    # print(f'#{t} {count}')