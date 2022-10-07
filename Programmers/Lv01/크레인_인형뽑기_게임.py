board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


stk = []

for val in board:
    print(val)

ans = 0

for val in moves:
    
    for i in range(len(board[0])):
        if board[val-1][i] != 0:
            print(i)
            if not stk:
                stk.append(board[val-1][i])
            else:
                if stk[-1] == board[val-1][i]:
                    stk.pop(-1)
                    ans+=2
                else:
                    stk.append(board[val-1][i])

            board[val-1][i] = 0
            break
    
    for val in board:
        print(val)
        
    print('############')


print(ans)

for val in board:
    print(val)