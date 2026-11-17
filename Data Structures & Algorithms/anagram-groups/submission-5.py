class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n) solution
        ourMap = {}

        for i in range(len(strs)):
            sorted_key = "".join(sorted(strs[i]))

            if sorted_key in ourMap:
                ourMap[sorted_key].append(strs[i]) 
            else:
                ourMap[sorted_key] = [strs[i]]
        
        return list(ourMap.values()) 


        # Brute Force Solution - O(n^2)
        '''
        visited = [False]*len(strs)
        answer = []

        for i in range(len(strs)):
            if visited[i] == True:
                continue

            group = []

            for j in range(i, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited[j] = True

            answer.append(group)
        
        return answer
        '''