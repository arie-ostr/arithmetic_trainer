nums = [1,1,2]

sum = 0
for num in nums:
    sum += num

mean = sum/len(nums)

sum_2 = 0
for num in nums:
    sum_2 += (mean-num)**2

var_sq = sum_2 / (len(nums)-1)


print(var_sq)