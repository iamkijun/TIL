N = int(input())

N_li = list(map(int, input().split()))
N_li.sort()

M = int(input())

M_li = list(map(int, input().split()))

def binary(arr,n,s,e):

    while s<=e:
        mid = (s+e)//2

        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            e = mid - 1
        else:
            s = mid + 1
    
    return None

for val in M_li:
    ans = binary(N_li,val,0,N-1)
    if ans != None:
        print('yes', end=" ")
    else:
        print('no', end=" ")

print()