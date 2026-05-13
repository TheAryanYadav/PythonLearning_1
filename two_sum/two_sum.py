class solutions:
    def two_sum(self,nums,target):
        for num1 in range(len(nums)):
            for num2 in range(num1+1,len(nums)):
                if (nums[num1]+nums[num2]==target):
                    return [num1,num2]


solve=solutions()
print(solve.two_sum([0,2,3,4,5,6],9))

