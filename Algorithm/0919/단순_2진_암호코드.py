import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input())) for _ in range(N)]

    num_arr = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

    start = 0

    for i in range(N):
        if 1 in arr[i]:
            while True:
                if arr[i][start:start+7] in num_arr:
                    break
                else:
                    start +=1
            li = []
            
            try:
                for j in range(8):
                    li.append(num_arr.index(arr[i][start:start+7]))
                    start += 7
            except:
                start = start - len(li)*7+2
                li = []
                
                for j in range(8):
                    li.append(num_arr.index(arr[i][start:start+7]))
                    start += 7


            val = (li[0]+li[2]+li[4]+li[6]) * 3 + (li[1]+li[3]+li[5]) +li[7]
            
            if val % 10 == 0:
                print(f'#{t} {sum(li)}')
            else:
                print(f'#{t} 0')

            break
    