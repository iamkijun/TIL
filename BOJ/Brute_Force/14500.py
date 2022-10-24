import sys
# input = sys.stdin.readline
sys.stdin = open('Brute_Force/input.txt','r')
'''
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
'''

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# ㅡㅡㅡㅡ
def one(i,j):
    global max_val

    if j <= M-4:
        one_1 = arr[i][j]
        one_2 = arr[i][j+1]
        one_3 = arr[i][j+2]
        one_4 = arr[i][j+3]
    
        current_val = one_1 + one_2 + one_3 + one_4

        max_val = max(max_val, current_val)

    if i <= N-4:
        one_1 = arr[i][j]
        one_2 = arr[i+1][j]
        one_3 = arr[i+2][j]
        one_4 = arr[i+3][j]
    
        current_val = one_1 + one_2 + one_3 + one_4

        max_val = max(max_val, current_val)

# ㅁ
def two(i,j):
    global max_val

    if i<= N-2 and j<= M-2:
        two_1 = arr[i][j]
        two_2 = arr[i][j+1]
        two_3 = arr[i+1][j]
        two_4 = arr[i+1][j+1]
    
        current_val = two_1 + two_2 + two_3 + two_4

        max_val = max(max_val, current_val)

def three(i,j):
    global max_val

    if i<= N-3 and j<= M-2:
        three_1 = arr[i][j]
        three_2 = arr[i+1][j]
        three_3 = arr[i+2][j]
        three_4 = arr[i+2][j+1]
    
        current_val = three_1 + three_2 + three_3 + three_4

        max_val = max(max_val, current_val)

    if i<= N-3 and j<= M-2:
        three_1 = arr[i][j]
        three_2 = arr[i][j+1]
        three_3 = arr[i+1][j+1]
        three_4 = arr[i+2][j+1]
    
        current_val = three_1 + three_2 + three_3 + three_4

        max_val = max(max_val, current_val)

    if i<= N-2 and j<= M-3:
        three_1 = arr[i+1][j]
        three_2 = arr[i+1][j+1]
        three_3 = arr[i+1][j+2]
        three_4 = arr[i][j+2]
    
        current_val = three_1 + three_2 + three_3 + three_4

        max_val = max(max_val, current_val)

    if i<= N-2 and j<= M-3:
        three_1 = arr[i][j]
        three_2 = arr[i][j+1]
        three_3 = arr[i][j+2]
        three_4 = arr[i+1][j]
    
        current_val = three_1 + three_2 + three_3 + three_4

        max_val = max(max_val, current_val)

    if i<= N-3 and j<= M-2:
        three_1 = arr[i][j+1]
        three_2 = arr[i+1][j+1]
        three_3 = arr[i+2][j+1]
        three_4 = arr[i+2][j]
    
        current_val = three_1 + three_2 + three_3 + three_4

        max_val = max(max_val, current_val)

    if i<= N-3 and j<= M-2:
        three_1 = arr[i][j]
        three_2 = arr[i+1][j]
        three_3 = arr[i+2][j]
        three_4 = arr[i][j+1]
    
        current_val = three_1 + three_2 + three_3 + three_4

        max_val = max(max_val, current_val)

    if i<= N-2 and j<= M-3:
        three_1 = arr[i][j]
        three_2 = arr[i+1][j]
        three_3 = arr[i+1][j+1]
        three_4 = arr[i+1][j+2]
    
        current_val = three_1 + three_2 + three_3 + three_4

        max_val = max(max_val, current_val)

    if i<= N-2 and j<= M-3:
        three_1 = arr[i][j]
        three_2 = arr[i][j+1]
        three_3 = arr[i][j+2]
        three_4 = arr[i+1][j+2]
    
        current_val = three_1 + three_2 + three_3 + three_4

        max_val = max(max_val, current_val)

def four(i,j):
    global max_val

    if i<= N-3 and j<= M-2:
        four_1 = arr[i][j]
        four_2 = arr[i+1][j]
        four_3 = arr[i+1][j+1]
        four_4 = arr[i+2][j+1]
    
        current_val = four_1 + four_2 + four_3 + four_4

        max_val = max(max_val, current_val)

    if i<= N-2 and j<= M-3:
        four_1 = arr[i+1][j]
        four_2 = arr[i][j+1]
        four_3 = arr[i+1][j+1]
        four_4 = arr[i][j+2]
    
        current_val = four_1 + four_2 + four_3 + four_4

        max_val = max(max_val, current_val)

    if i<= N-3 and j<= M-2:
        four_1 = arr[i][j+1]
        four_2 = arr[i+1][j]
        four_3 = arr[i+1][j+1]
        four_4 = arr[i+2][j]
    
        current_val = four_1 + four_2 + four_3 + four_4

        max_val = max(max_val, current_val)

    if i<= N-2 and j<= M-3:
        four_1 = arr[i+1][j+2]
        four_2 = arr[i][j+1]
        four_3 = arr[i+1][j+1]
        four_4 = arr[i][j]
    
        current_val = four_1 + four_2 + four_3 + four_4

        max_val = max(max_val, current_val)

def five(i,j):
    global max_val

    if i<= N-2 and j<= M-3:
        five_1 = arr[i][j]
        five_2 = arr[i][j+1]
        five_3 = arr[i][j+2]
        five_4 = arr[i+1][j+1]
    
        current_val = five_1 + five_2 + five_3 + five_4

        max_val = max(max_val, current_val)

    if i<= N-2 and j<= M-3:
        five_1 = arr[i+1][j]
        five_2 = arr[i+1][j+1]
        five_3 = arr[i+1][j+2]
        five_4 = arr[i][j+1]
    
        current_val = five_1 + five_2 + five_3 + five_4

        max_val = max(max_val, current_val)
    
    if i<= N-3 and j<= M-2:
        five_1 = arr[i][j]
        five_2 = arr[i+1][j]
        five_3 = arr[i+2][j]
        five_4 = arr[i+1][j+1]
    
        current_val = five_1 + five_2 + five_3 + five_4

        max_val = max(max_val, current_val)

    if i<= N-3 and j<= M-2:
        five_1 = arr[i][j+1]
        five_2 = arr[i+1][j+1]
        five_3 = arr[i+2][j+1]
        five_4 = arr[i+1][j]
    
        current_val = five_1 + five_2 + five_3 + five_4

        max_val = max(max_val, current_val)





max_val = 0
for i in range(N):
    for j in range(M):
        one(i,j)
        two(i,j)
        three(i,j)
        four(i,j)
        five(i,j)

print(max_val)