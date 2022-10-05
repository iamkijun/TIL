nums = [-1,0,1,2,-1,-4]
nums.sort()
li = []

for i in range(len(nums)-2):
    for j in range(i,len(nums)-1):
        for k in range(j, len(nums)):
            if i!= j!= k and nums[i] + nums[j] + nums[k] == 0:
                ele = [nums[i],nums[j],nums[k]]
                ele.sort()
                if ele in li:
                    continue
                else:
                    li.append(ele)

print(li)