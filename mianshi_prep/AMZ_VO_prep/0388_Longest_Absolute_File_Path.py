class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maximum = 0
        path = {0:0}
        for line in input.splitlines():
            curr = line.lstrip('\t')
            depth = len(line) - len(curr)
            if '.' in curr:
                maximum = max(maximum, path[depth]+len(curr))

            else:
                path[depth+1] = path[depth] + len(curr) + 1

        return maximum
