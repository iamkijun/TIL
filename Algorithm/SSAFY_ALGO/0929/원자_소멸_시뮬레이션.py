import sys
sys.stdin = open('input.txt','r')
'''
2
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
4
-1 1 3 3
0 1 1 1
0 0 2 2
-1 0 0 9
'''
T = int(input())

di = [-1,1,0,0]
dj = [0,0,-1,1]

for t in range(1,T+1):

    N = int(input())

    for i in range(N):
        x, j, dir, K = map(int, input().split())



    print(f'#{t} ')