

class Solution:
    def findMin(self, nums) :
        l = len(nums)
        m = l//2
        if (nums[0] <= nums[-1]):
            print("true")
            return nums[0]
        left = nums[0:m]
        print(left)
    
        right= nums[m:l]
        print(right)
        return min(self.findMin(left), self.findMin(right))
        
nums = [4,5,6,7,0,1,2]
s = Solution()
print(s.findMin(nums))
#print(s)



