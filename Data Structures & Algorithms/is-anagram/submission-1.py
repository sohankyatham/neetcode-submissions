class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) solution using hash map


        # O(nlogn) - sort both lists and compare; sorted(...) takes O(nlog n) 
        
        s = sorted(s)
        t = sorted(t)
        if s == t: # this is O(n)
            return True
        else:
            return False 
        

        # O(n^2) solution
        '''
        if len(s) != len(t):
            return False

        t_list = list(t)

        for char in s:
            if char in t_list:
                t_list.remove(char) # O(n) operation inside O(n) loop
            else:
                return False
        return True 
        '''

        # O(n^2) [passes both cases but not correct solution] 
            # doesn't account for edge case if there are duplicate values
            # only checks presence not frequencies 
        '''
        if len(s) == len(t):
            for char in s:
                if not char in t: # O(n) operation inside O(n) loop
                    return False
            return True 
        return False
        '''