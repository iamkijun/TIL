import sys
sys.stdin = open('IM추천문제/input.txt','r')

for t in range(4):

    ax,ay,bx,by, cx,cy,dx,dy = map(int ,input().split())

    if ax > dx or ay > dy or bx < cx or by < cy:
        print('d')
    elif (cx==bx and cy==by) or (ax==dx and ay==dy) or (cx==bx and ay==dy) or (ax==dx and cy==by):
        print('c')
    elif ax == dx or bx == cx or ay == dy or by == cy:
        print('b')
    else:
        print('a')