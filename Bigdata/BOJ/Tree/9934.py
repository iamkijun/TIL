import sys
sys.stdin = open('Tree/input.txt','r')

K = int(input())

li = list(map(int, input().split()))

tree = [[] for _ in range(K)]

ino = []
def find_tree(first, last,k):
    if first == last:
        tree[k].append(li[first])
        return
    
    mid = (first + last)//2
    tree[k].append(li[mid])
    find_tree(first,mid-1,k+1)
    find_tree(mid+1,last,k+1)

find_tree(0,len(li)-1,0)

for i in range(K):
    for val in tree[i]:
        print(val, end=' ')
    print()
