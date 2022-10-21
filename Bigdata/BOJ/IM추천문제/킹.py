import sys
sys.stdin = open('IM추천문제/input.txt','r')

king, dol, N = input().split()

# 킹과 돌을 숫자 좌표로 변경
king = [ord(king[0]) - 64, int(king[1])]
dol = [ord(dol[0]) - 64, int(dol[1])]

for n in range(int(N)):

    # 움직임도 좌표로 변경
    m = input()
    go = [0, 0]
    for val in m:
        if val == 'R':
            go[0] += 1
        elif val == 'L':
            go[0] -= 1
        elif val == 'B':
            go[1] -= 1
        elif val == 'T':
            go[1] += 1

    # 킹과 돌이 좌표를 벗어나지 않는다면 이동
    go_king = [king[0] + go[0], king[1] + go[1]]

    if go_king == dol:
        go_dol = [dol[0] + go[0], dol[1] + go[1]]
        if 0 in go_dol or 9 in go_dol:
            continue
        else:
            dol = go_dol

    if 0 in go_king or 9 in go_king:
        continue
    else:
        king = go_king

# 숫자 좌표를 다시 일반 좌표로 변경하여 출력
king = chr(king[0] + 64) + str(king[1])
rock = chr(dol[0] + 64) + str(dol[1])
print(king)
print(rock)