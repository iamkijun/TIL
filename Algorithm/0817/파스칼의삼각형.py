import sys
sys.stdin = open("0817/input.txt","r")

T = int(input())

def tri(a):
    if a == 1:
        arr= [[1]]
        return arr
    elif a == 2:
        arr = [[1],[1,1]]
        return arr
    else:
        arr = [[1],[1,1]]
        for i in range(2,a):
            li = [0] * (i + 1)

            for j in range(i+1):
                if j == 0 or j == i:
                    li[j] = 1
                else:
                    li[j] = arr[i-1][j-1] + arr[i-1][j]
            
            arr.append(li)

        return arr

for t in range(1, T+1):
    N = int(input())
    print(f'#{t}')
    
    triangle = tri(N)
    
    for i in range(N):
        print(*triangle[i])