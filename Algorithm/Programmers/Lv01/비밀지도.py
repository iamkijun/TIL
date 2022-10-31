def solution(n, arr1, arr2):
    new_arr1 = []
    new_arr2 = []
    for val in arr1:
        temp =[0] *n
        for i in range(n):
            if val >= 2**(n-1-i):
                temp[i] = 1
                val -= 2**(n-1-i)
        new_arr1.append(temp)

    for val in arr2:
        temp =[0]*n
        for i in range(n):
            if val >= 2**(n-1-i):
                temp[i] = 1
                val -= 2**(n-1-i)
        new_arr2.append(temp)

    answer =[]

    for i in range(n):
        temp = ''
        for j in range(n):
            if new_arr1[i][j] == 1 or new_arr2[i][j] == 1:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer