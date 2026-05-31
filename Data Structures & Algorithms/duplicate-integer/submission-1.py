class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if prev == curr:
                return True
            prev = curr
        return False