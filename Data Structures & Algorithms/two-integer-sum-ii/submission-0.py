class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 1
        index2 = len(numbers)
        while index1 <= index2:
            if numbers[index1-1] + numbers[index2-1] == target:
                return [index1, index2]
            elif numbers[index1-1] + numbers[index2-1] > target:
                index2 -= 1
            else:
                index1 +=1
        