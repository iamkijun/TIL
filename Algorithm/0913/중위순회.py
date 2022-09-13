import sys
sys.stdin = open('input.txt','r')

def inorder(n):
    for i in range(n):
        
        inorder(n*2)  # Left
        li = list(map(str, input().split()))
        ch[n] = li[1]
        inorder(n*2 + 1)


for t in range(1,11):
    N = int(input())
    ch = [''] * (N+1)
    # 완전이진트리 생성(inorder)
    inorder(N)
    
    print(f'#{t}', *ch[1:])
