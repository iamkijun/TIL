board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0

    stk = []
    for val in moves:
        for i in range(len(board[0])):
            if board[i][val-1]:
                stk.append(board[i][val-1])
                board[i][val-1] = 0
                break

        while stk:
            if len(stk) >= 2 and stk[-1] == stk[-2]:
                stk.pop(-1)
                stk.pop(-1)
                answer += 2
            else:
                break
    
    return answer

print(solution(board, moves))