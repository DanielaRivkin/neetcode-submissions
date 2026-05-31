class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_counter = Counter(nums)
        most_common = my_counter.most_common(k)
        output = [item[0] for item in most_common]
        return output