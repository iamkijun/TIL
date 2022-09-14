import sys
sys.stdin = open('Tree/input.txt','r')

N = int(input())

dic = {}

for i in range(1,N+1):
    parent, left, right = map(str, input().split())

    dic[parent] = [left, right]

root = 'A'

pre = []
def preorder(n):
    if n != '.':
        pre.append(n)
        preorder(dic[n][0])
        preorder(dic[n][1])

preorder(root)
print(''.join(pre))

ino = []
def inorder(n):
    if n != '.':
        inorder(dic[n][0])
        ino.append(n)
        inorder(dic[n][1])

inorder(root)
print(''.join(ino))

pos = []
def postorder(n):
    if n != '.':
        postorder(dic[n][0])
        postorder(dic[n][1])
        pos.append(n)

postorder(root)
print(''.join(pos))
