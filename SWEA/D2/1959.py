T = int(input())

for k in range(T):
    N, M = map(int, input().split())

    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    
    max = 0

    if N<M:
        a = M-N
        for j in range(0,a+1):
            sum = 0
            new = 0
            for i in range(N):
                sum = n[i]*m[i+j]
                new += sum
            if new > max:
                    max = new    

    elif N>M:
        a = N-M
        for j in range(0,a+1):
            sum = 0
            new = 0
            for i in range(M):
                sum = n[i+j]*m[i]
                new += sum
            if new > max:
                    max = new    
            
    print("#%d %d"%(k+1,max))