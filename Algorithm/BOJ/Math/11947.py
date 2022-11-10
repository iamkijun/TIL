import sys
sys.stdin = open('Math/input.txt','r')

T = int(input())

for t in range(T):
    n = input()
    ans = ''
    for i in range(len(n)-1,-1,-1):
        ans = str(9-int(n[i])) + ans
    
    print(int(ans)*int(n))