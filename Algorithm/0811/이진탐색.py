import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def binarySearch(total,key):
    start = 1
    end = total
    count =0
    while start <= end:
        middle = int((start+end)//2)
        if middle == key:
            break
        elif middle > key:
            end = middle
            count+=1
        elif middle < key:
            start= middle
            count +=1
    return count

for t in range(1,T+1):
    P, A, B = map(int, input().split())
    A_count = binarySearch(P,A)
    B_count = binarySearch(P,B)

    if A_count < B_count:
        print(f'#{t} A')
    elif B_count < A_count:
        print(f'#{t} B')
    elif A_count == B_count:
        print(f'#{t} 0')