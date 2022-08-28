import sys
sys.stdin = open('input.txt','r')

N, M = map(int, input().split())
N_list = []
for i in range(1,N+1):
    N_list.append(i)

x_list=[0] * M
for x in range(M):
    a, b = map(int,input().split())
    x_list[x] = [a,b]


count = 0

for i in range(1<<N):
    li = []
    for j in range(N):
        if i & (1<<j):
            li.append(N_list[j])
    
    

    if len(li) == 3:
        ans = 0
        for k in range(M):
            if set(x_list[k]) < set(li):        
                ans+=1
        if ans == 0:
            count +=1
        
        ans = 0
            
print(count)