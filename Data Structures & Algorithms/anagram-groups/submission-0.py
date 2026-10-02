class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {} # dict to match groups

        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            
            groups[key].append(s)
        
        return list(groups.values())


        # sort s --> sorted(s)
        # sorted(s) --> .join
        # key not in groups --> create []
        # append --> []
