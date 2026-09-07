class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # O(n) solution - comparing length of set to length of list
        
        if len(set(nums)) == len(nums):
            return False
        return True
        

        # O(n) solution - using empty set 
        '''
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        '''

        # O(n^2) solution
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    return True

        return False
        '''