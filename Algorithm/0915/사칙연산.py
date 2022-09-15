import sys
sys.stdin = open('input.txt','r')

def postorder(n):
    if 0< n <= N:
        if ans[n][1] == '+':
            return postorder(int(ans[n][2]))+postorder(int(ans[n][3]))
        elif ans[n][1] == '-':
            return postorder(int(ans[n][2]))-postorder(int(ans[n][3]))
        elif ans[n][1] == '*':
            return postorder(int(ans[n][2]))*postorder(int(ans[n][3]))
        elif ans[n][1] == '/':
            return postorder(int(ans[n][2]))/postorder(int(ans[n][3]))
        else:
            return int(ans[n][1])
    else:
        return 0

for t in range(1,2):

    N = int(input())

    ans = [[0]]

    for i in range(1,N+1):
        li = list(map(str, input().split()))
        ans.append(li)
    print(ans)
    result = postorder(1)

    print(f'#{t} {int(result)}')