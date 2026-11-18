class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourMap = {}

        # 1) loop thru the list and add unique elements as keys
        # 2) recurring elements should updatae the count (value)
        for i in range(len(nums)):
            if nums[i] in ourMap:
                ourMap[nums[i]] = ourMap.get(nums[i], 0) + 1    # increment the count
            else:
                ourMap[nums[i]] = 1

        # '''
        # more pythonic way consider this:

        # for num in nums:
        #     ourMap[num] = ourMap.get(num,0) + 1
        # '''

        # 3) return the top k
        sorted_map = sorted(ourMap.items(), key=lambda x: x[1], reverse=True)

        answer = []
        for i in range(k):
            answer.append(sorted_map[i][0])
        
        return answer