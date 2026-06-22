class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1,d2={},{}
        for i,j in zip_longest(s,t):
            if i not in d1.keys():
                d1[i]=1
            else: d1[i]+=1
            if j not in d2.keys():
                d2[j]=1
            else: d2[j]+=1
        for i in d1.keys():
            if i not in d2.keys(): return False
            if d1[i]!=d2[i]: return False
        return True