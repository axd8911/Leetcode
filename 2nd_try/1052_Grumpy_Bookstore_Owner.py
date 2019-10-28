class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # roll the index, get the maximum amount
        maximum = 0
        curr = 0
        idx = collections.deque([])
        total = 0
        for i in range(len(customers)):
            idx.append(i)
            if grumpy[i] == 1:
                curr += customers[i]
                total += customers[i]
            if i >= X:
                left = idx.popleft()
                if grumpy[left] == 1:
                    curr -= customers[left]
            maximum = max(maximum,curr)

        return sum(customers) - total + maximum
