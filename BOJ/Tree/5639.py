import sys
sys.stdin = open('Tree/input.txt','r')

'''
50
30
24
5
28
45
98
52
60
'''

def postorder(n):
    

    postorder(n*2)
    postorder(n*2+1)
    print(n, end=" ")

tree = []

while True:
    try:
        n = int(input())
        tree.append(n)
    except:
        break
print(tree)

arr = []