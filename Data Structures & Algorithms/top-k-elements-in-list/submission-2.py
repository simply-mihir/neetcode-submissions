from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        top_k=heapq.nlargest(k,freq.keys(), key= lambda x: freq[x])
        return top_k
