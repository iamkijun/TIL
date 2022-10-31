import sys
sys.stdin = open("Greedy/input.txt","r")

T = int(input())

for t in range(T):
    K = int(input())
    li= list(map(int, input().split()))
    li.sort()
    ans = 0
    if K % 2 == 1:
        li.append(li.pop(0) + li.pop(1))
        ans += li[-1]
        li.sort()
    
    while K>1:
        K = K//2
        ans += sum(li)
        
        
    print(sum(li))
    print(ans)