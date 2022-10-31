import copy as cp

N = int(input())

min = N
ver = N

while ver!=0:
    ver_copy = cp.deepcopy(ver)
    ver_val = ver_copy

    while ver_copy !=0:
        ver_val += ver_copy%10
        ver_copy = ver_copy//10
    
    if ver_val == N:
        min = ver
    else:
        pass
    
    ver = ver-1
    

if min == N:
    print(0)
else:
    print(min)