class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # O(n) solution as well but more pythonic and cleaner
        return nums * 2
        
        # O(n) solution
        '''
        for i in range(len(nums)):
            nums.append(nums[i])

        return nums
        '''