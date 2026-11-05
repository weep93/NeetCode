from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorts = sorted(nums)
        counts = dict(Counter(sorts))
        sorted_items = sorted(
            counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [item[0] for item in sorted_items[:k]]