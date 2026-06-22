class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            a=[0]*26
            for j in i:
                a[26-(123-ord(j))]+=1
            if tuple(a) not in d.keys():
                d[tuple(a)]=[i]
            else:
                d[tuple(a)]+=[i]
        return list(d.values())
