# arr= [1,2,3,4,5,6]
#
# n=6
#
# for i in range(1<<6):
#     for j in range(6):
#         if i& (1<<j):
#             print(arr[j], end=", ")
#     print()
# print()

# def binarySearch(total,key):
#     start = 0
#     end = total
#     count =0
#     while start <= end:
#         middle = (start+end)//2
#         if middle == key:
#             break
#         elif middle > key:
#             end = middle -1
#             count+=1
#         else:
#             start= middle +1
#             count +=1
#
#     return count
# print(binarySearch(400,350))

def selectionSort(a,N):
    for i in range(N-1):
        maxIdx = i
        minIdx = i
        if i % 2 == 0:
            for j in range(i+1,N):
                if a[maxIdx] < a[j]:
                    maxIdx = j
            a[i], a[maxIdx] = a[maxIdx], a[i]

        elif i % 2 == 1:
            for j in range(i+1,N):
                if a[minIdx] > a[j]:
                    minIdx = j
            a[i], a[minIdx] = a[minIdx], a[i]

    return a

print(selectionSort([1,2,3,4,5],5))