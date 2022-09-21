import sys
sys.stdin = open('input.txt','r')

def dfs(count):
    global ans

    if count == 0:
        ans = max(int(''.join(li)),ans)
        return
    
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            #바꿔줬다가,
            li[i],li[j] = li[j],li[i]
            temp = ''.join(li)
            if visited.get((temp,count-1),1):
                visited[(temp,count-1)]=0
                dfs(count-1)
            #다시 원위치,
            li[i],li[j] = li[j],li[i]


T = int (input())

for t in range(1,T+1):

    N, trial = input().split()

    li = list(N)

    trial = int(trial)

    visited = {}
    ans = 0
    dfs(trial)
    
    print(f'#{t}',ans)