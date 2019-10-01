class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr)>1:
            idx = arr.index(min(arr))
            if idx==0:
                res += arr[0]*arr[1]
            elif idx==len(arr)-1:
                res += arr[idx]*arr[idx-1]
            else:
                res += arr[idx]*min(arr[idx-1],arr[idx+1])
            arr.pop(idx)
        return res
