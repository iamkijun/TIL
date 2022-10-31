import sys
from turtle import circle
sys.stdin = open('input.txt','r')

N = int(input())

for n in range(N):

    # [1] 원소들의 갯수 탐색
    A = list(map(int, input().split()))
    A.pop(0)
    a_star ,a_circle, a_square, a_triangle = 0,0,0,0

    for val in A:
        if val == 4:
            a_star +=1
        elif val == 3:
            a_circle +=1
        elif val == 2:
            a_square +=1
        elif val == 1:
            a_triangle +=1 
    
    B = list(map(int, input().split()))
    B.pop(0)
    b_star ,b_circle, b_square, b_triangle = 0,0,0,0

    for val in B:
        if val == 4:
            b_star +=1
        elif val == 3:
            b_circle +=1
        elif val == 2:
            b_square +=1
        elif val == 1:
            b_triangle +=1 
    
    # [2] 원소들의 갯수 비교
    if a_star > b_star:
        print("A")
    elif b_star > a_star:
        print("B")

    else:
        if a_circle > b_circle:
            print("A")
        elif b_circle > a_circle:
            print("B")

        else:
            if a_square > b_square:
                print("A")
            elif b_square > a_square:
                print("B")

            else:
                if a_triangle > b_triangle:
                    print("A")
                elif b_triangle > a_triangle:
                    print("B")
                else:
                    print("D")
