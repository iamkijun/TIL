import sys
sys.stdin = open('Tree/input.txt','r')

K = int(input())

li = list(map(int, input().split()))

ino = []
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)            # visit(n)
        inorder(ch2[n])

for i in range(2**K-1):
    li[i] 
