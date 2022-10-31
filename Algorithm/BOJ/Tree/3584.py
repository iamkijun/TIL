import sys
# input=sys.stdin.readline
sys.stdin = open('Tree/input.txt','r')


T = int(input())

def backtracking(n1,li):
    li.append(n1)
    i= 1
    while i <= N:
        if n1 in arr[i]:
            li.append(i)
            n1 = i
            i =1
            continue
        i+=1
    return li

def find_backtracking(n2,li):
    global n1
    
    i =1
    while i <= N:
        if n2 in li1:
            return n2
        if n2 in arr[i]:
            li.append(i)
            n2 = i
            i = 1
            continue
        i+=1    


for t in range(1,T+1):

    N = int(input())
    arr = [0] * (N+1)

    for i in range(N-1):
        A, B = map(int, input().split())
        arr[B] = A
    
    node1, node2 = map(int, input().split())

    node1_li =[node1]
    node2_li =[node2]

    while arr[node1]:
        node1_li.append(arr[node1])
        node1 = arr[node1]
    while arr[node2]:
        node2_li.append(arr[node2])
        node2 = arr[node2]

    # print(node1_li,node2_li)

    i= 1
    while i<= min([len(node1_li), len(node2_li)]) and node1_li[-i] == node2_li[-i]:
        i+=1
    print(node1_li[-i+1])

'''
2
16
1 14
8 5
10 16
5 9
4 6
8 4
4 10
1 13
6 15
10 11
6 7
10 2
16 3
8 1
16 12
16 7
5
2 3
3 4
3 1
1 5
3 5
'''

# T = int(input())

# def backtracking(n1,li):
#     li.append(n1)
#     i= 1
#     while i <= N:
#         if n1 in arr[i]:
#             li.append(i)
#             n1 = i
#             i =1
#             continue
#         i+=1
#     return li

# def find_backtracking(n2,li):
#     global n1
    
#     i =1
#     while i <= N:
#         if n2 in li1:
#             return n2
#         if n2 in arr[i]:
#             li.append(i)
#             n2 = i
#             i = 1
#             continue
#         i+=1    


# for t in range(1,T+1):

#     N = int(input())
#     arr = [[] for _ in range(N+1)]

#     for i in range(N-1):
#         A, B = map(int, input().split())
#         arr[A].append(B)

#     node1, node2 = map(int, input().split())

#     li1 = []
#     li1 = backtracking(node1,li1)
    
#     li2 = []
#     ans = find_backtracking(node2,li2)
#     print(ans)
    