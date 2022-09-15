import sys
sys.stdin = open('Tree/input.txt','r')

tree = [0]
idx = 1
while True:
    try:
        n = int(input())

        tree.append(n)

        idx += 1
    except:
        break
ch1 = [0] * len(tree)
ch2 = [0] * len(tree)

for idx,val in enumerate(tree):
    if idx < 
    print(idx,val)
    

def postorder(n):
    if 2*n+1 <= len(tree)-1:
        postorder(tree[2*n])
        postorder(tree[2*n+1])
        print(n)

postorder(1)