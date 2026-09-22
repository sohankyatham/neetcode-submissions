class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map with one pass - O(n)
        ourMap = {}

        for i in range(len(nums)):
            need = target - nums[i]   # find what is needed to add up to target

            # search in hashmap
            if need in ourMap:
                return [ourMap[need], i] 
  
            ourMap[nums[i]] = i     # Add to hashmap

        return []



        
        # Hash map with two passes - O(n)
        '''
        ourMap = {}

        # First add everything to the hash map
        for i in range(len(nums)):
            ourMap[nums[i]] = i

        # Then check what is needed
        for i in range(len(nums)):
            need = target - nums[i]
            if (need in ourMap) and (ourMap[need] != i):
                return [i, ourMap[need]]
        return []
        '''


        # Brute force solution w/ two for loops - O(n^2)
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
        return []
        '''