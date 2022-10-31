maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

def dfs(i,j,answer):
    if i == 0 and j == 0:
        return

    for di, dj in ((0, 1), (1, 0)):
        ni, nj = i + di, j + dj
        if 0 <= ni < 5 and 0 <= nj < 5 and maps[ni][nj] == 1:
            maps[ni][nj] = 1
            answer += 1
            dfs(ni,nj,answer)


def solution(maps):
    answer = 0

    q= []
    q.append([len(maps[0]-1),len(maps[0]-1)])



    return answer



print(solution(maps))