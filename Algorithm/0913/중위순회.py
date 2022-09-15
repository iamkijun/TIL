import sys
sys.stdin = open('input.txt','r')

def inorder(n):
    global ans

    if n <= N:  # 존재하는 노드인 경우 처리
        inorder(n * 2)  # Left
        ans += ch[n]
        inorder(n * 2 + 1)


for t in range(1, 11):
    N = int(input())
    ch = [0] * (N + 1)
    # 완전이진트리 생성(inorder)
    for i in range(1, N + 1):
        li = list(map(str, input().split()))
        ch[int(li[0])] = li[1]

    ans = ''

    inorder(1)

    print(f'#{t}', ans)