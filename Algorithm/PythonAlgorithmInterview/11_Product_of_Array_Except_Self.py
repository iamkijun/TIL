nums =[1,2,3,4]
new =[]

for i in range(len(nums)):
    fake_nums = nums[:i]+nums[i+1:]

    multi = 1
    for j in range(len(nums)-1):
        multi *= fake_nums[j]

    new.append(multi)
    print(new)