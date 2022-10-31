sys.stdin = open("D3/input.txt","r")

T = int(input())

for t in range(1, T+1):
    li = list(map(int, input().split()))
    a = li[0]
    b = li[1]
    a = list(str(a))

    for i in range(b):
        for j in range(len(a)-1):
            maxIdx = j
            for k in range(i, len(a)):
                if int(a[maxIdx]) <= int(a[k]):
                    maxIdx = k
        
            a[maxIdx], a[i] = a[i], a[maxIdx]
    
    print(a)