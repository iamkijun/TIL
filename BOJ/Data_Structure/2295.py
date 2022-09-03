import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

N = int(input())
li = [0] * N
for i in range(N):
    li[i] = int(input())

max_V =0

def find_max(li):
    for i in range(N-1,1,-1):
        for j in range(i-1,0,-1):
            for k in range(j-1,-1,-1):
                if li[i]+li[j]+li[k] in li:
                    return li[i]+li[j]+li[k]

print(find_max(li))