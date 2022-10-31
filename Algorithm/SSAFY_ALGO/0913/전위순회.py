import sys
sys.stdin = open('input.txt','r')

T = int(input())

def preorder(n):
    global ans
    if n:
        ans.append(n)
        preorder(ch1[n])
        preorder(ch2[n])

for t in range(1,T+1):
    

    V = int(input())
    arr = list(map(int, input().split()))
    # 부모를 인덱스로 자식 번호 저장
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    
    for i in range(0,2*V-2,2):
        p, c = arr[i], arr[i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    ans = []
    preorder(1)
    
    print(f'#{t}', *ans)

    