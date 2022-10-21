import sys
sys.stdin = open("Graph/input.txt","r")
'''
........
........
........
........
........
........
........
........
'''

arr = [list(input()) for _ in range(8)]

ci, cj = 7, 0

def right_up(ci,cj):
    global q
    q.append([ci,cj])

    while q:
        ci, cj = q.pop(0)

        if ci==0 and cj==7:
            return 1

        for di,dj in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):         #우,우상,상으로 이동

            ni, nj = ci+di, cj+dj

            if 0<=ni<8 and 0<=nj<8 and arr[ni][nj] == '.':      #범위 내, 이동 가능
                if ni>=1:                                       #위에 벽인지 확인
                    if arr[ni-1][nj] == '.':                    #위에 벽이 아니면
                        q.append([ci,cj])                       #이동 가능
                    else:                                       #위에 벽이면
                        continue                                #이동 불가능, 다른경로 탐색
                elif ni == 0:
                    q.append([ci,cj])
                
        print(ci,cj)

    return 0

q =[]
print(right_up(7,0))