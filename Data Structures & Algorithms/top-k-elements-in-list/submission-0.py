class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # unique = dict()
        # for num in nums:
        #     if num in unique:
        #         unique[num] += 1
        #     else:
        #         unique[num] = 1
        my_counter = Counter(nums)
        most_common = my_counter.most_common(k)
        output = [item[0] for item in most_common]
        return output