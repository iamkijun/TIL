import sys
sys.stdin = open('input.txt','r')

for t in range(4):

    lx1,ly1,lx2,ly2, rx1,ry1,rx2,ry2 = map(int,input().split())

    if lx2 < rx1 or ly2 < ry1:
        print("d")
    
    elif lx2 > rx1 and ly2 > ry1:
        print("a")

    elif lx2 == rx1 and ly2> ry1:
        print("b")
    elif lx2 > rx1 and ly2 == ry1:
        print("b")

    elif lx2 == rx1 and ly1 == ry2:
        print("c")
    elif lx2 == rx1 and ly2 == ry1:
        print("c")

    
