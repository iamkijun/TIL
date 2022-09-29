import sys
# input = sys.stdin.readline
sys.stdin = open('Data_Structure/input.txt')

n, m = map(int, input().split())

new_li=[]
for i in range(m):
    check, a, b = map(int, input().split())

    if check == 0:
        for i in range(n):
            new = set.union(set(a),set(b))
            for val in new_li:
                if a in val:
                    idx1 = val
                if b in val:
                    idx2 = val

    elif check == 1:
        for val in arr:
            if a in val and b in val:
                print('YES')
                break
        else:
            print('NO')