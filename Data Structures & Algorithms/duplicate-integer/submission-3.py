class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # Pushed right by 8 spaces because it's inside the function
        uni_bg = set(nums)
        
        print("what a set looks", uni_bg)
        
        if len(uni_bg) < len(nums):
            return True
        else:
            return False