class Solution(object):
    def containsDuplicate(self,nums):
        nums1=set()
        for number in nums:
            if number in nums1:
                return True
            nums1.add(number)
        return False
    
solve=Solution()
print(solve.containsDuplicate([1,2,3,4,5,1]))
            