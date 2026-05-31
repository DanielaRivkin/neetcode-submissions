# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Handle the edge case where the input list is empty
        if not pairs:
            return []  # Return an empty list if there are no pairs to sort
        
        snapshots = [pairs[:]]  # Add the initial state of the list as the first snapshot
        for i in range(1, len(pairs)):
            current = pairs[i]  # The current element to be inserted
            j = i - 1
            # Shift elements in the sorted portion to make space for `current`
            while j >= 0 and pairs[j].key > current.key:
                pairs[j + 1] = pairs[j]  # Shift the element to the right
                j -= 1
            pairs[j + 1] = current  # Place `current` in its correct position
            # Take a snapshot of the current state of the list
            snapshots.append(pairs[:])  # Append a copy of the list to avoid mutability issues
        return snapshots
