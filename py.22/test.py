class Solution:
    def firstMissingPositive(self, nums):
        # a = 1
        # if len(nums) == 1 and a in nums:
        #     return a + 1
        
        
        for x in range(1,len(nums)):
            if x not in nums:return x
                 
            

a = Solution()
print(a.firstMissingPositive([1,2,0]))
        
            









        # a = str(a)
        # q = []
        # for i in a:
        #     i = int(i)
        #     digits.append(i)
        # return digits





# print(s.plusOne([9]))

