numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand= "right"

arr = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

def solution(numbers, hand):
    answer = ''

    current_L = '*'
    current_R = '#'
    current = [0,0]
    _L = [3,0]
    _R = [3,2]

    L_distance = 0
    R_distance = 0

    for val in numbers:

        if val in [1,4,7]:
            answer += 'L'
            current_L = val

        elif val in [3,6,9]:
            answer += 'R'
            current_R = val
        
        else:
            for i in range(4):
                for j in range(3):
                    if arr[i][j] == val:
                        current = [i,j]
                    if arr[i][j] == current_L:
                        _L = [i,j]
                    if arr[i][j] == current_R:
                        _R = [i,j]
            
            L_distance = abs(current[0]-_L[0]) + abs(current[1]-_L[1])
            R_distance = abs(current[0]-_R[0]) + abs(current[1]-_R[1])

            if L_distance < R_distance:
                answer += 'L'
                current_L = val

            elif R_distance < L_distance:
                answer += 'R'
                current_R = val

            else:
                if hand == 'left':
                    answer += 'L'
                    current_L = val
                elif hand == 'right':
                    answer += 'R'
                    current_R = val

    return answer

print(answer)

