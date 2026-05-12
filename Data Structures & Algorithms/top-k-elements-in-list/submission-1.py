class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        arr = []

        # Store frequency and number
        for num in count:
            arr.append([count[num], num])

        # Sort frequencies
        arr.sort()

        res = []

        # Get top k elements
        while len(res) < k:
            res.append(arr.pop()[1])

        return res