class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in hashMap:
                hashMap[sort]= []
                hashMap[sort].append(s)
            else:
                hashMap[sort].append(s)
        return list(hashMap.values())