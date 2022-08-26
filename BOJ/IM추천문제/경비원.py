import sys
sys.stdin = open('input.txt','r')

W, H = map(int, input().split())

n = int(input())

store_list = []         #가게 이름이라고 변수명을 지었지만 마지막에 나의 위치도 포함
for _ in range(n+1):
    dir, dis = map(int, input().split()) # dir:방향, dis:거리
    if dir == 1:
        store_list.append([dir,H,dis])      #방향에 따라 좌표 설정
    elif dir == 2:
        store_list.append([dir,0,dis])
    elif dir == 3:
        store_list.append([dir,H-dis, 0])
    elif dir == 4:
        store_list.append([dir,H-dis, W])

my_location = store_list.pop(-1)        #나의 위치를 따로 선언

fast_sum = 0 #최단거리 합
for i in range(n):
    #방향이 좌/우, 상/하 대칭인지 확인해보기위해
    list_dir = [store_list[i][0], my_location[0]]
    list_dir.sort()

    #방향이 대칭일경우,
    if list_dir == [1,2]:
        #상하 대칭이면 높이+왼쪽에서 좌표의 거리, 높이+오른쪽에서 좌표의 거리 가운데 최소값을 최단거리에 저장
        fast_sum += min([H+store_list[i][2]+my_location[2],H+(2*W-store_list[i][2]-my_location[2])])
    elif list_dir == [3,4]:
        #좌우 대칭이면 너비+아래에서 좌표의 거리, 너비+위에서 좌표의 거리 가운데 최솟값을 최단거리에 저장
        fast_sum += min([W+store_list[i][1]+my_location[1],W+(2*H-store_list[i][1]-my_location[1])])
        #그 외에 경우에는 그냥 좌표들간의 차이가 최단거리가 됨
    else:
        fast_sum += (abs(store_list[i][1]-my_location[1])+abs(store_list[i][2]-my_location[2]))


print(fast_sum)


