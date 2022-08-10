import sys
sys.stdin = open("s_input.txt","r")


import random

h_list = []

for i in range(9):
    height = int(input())
    h_list.append(height)

while True:
    ran_li = random.sample(h_list,7)
    if sum(ran_li) == 100:
        ran_li.sort()
        for v in ran_li:
            print(v)
        break
