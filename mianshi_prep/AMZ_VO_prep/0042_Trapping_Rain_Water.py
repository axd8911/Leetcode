class Solution:
    def trap(self, height: List[int]) -> int:
        # update highest in left and highest in right

        l = 0
        r = len(height)-1

        lmax = rmax = 0

        total = 0

        while l<=r:

            if height[l]<height[r]:
                lmax = max(lmax,height[l])
                total += lmax - height[l]
                l+=1

            else:
                rmax = max(rmax,height[r])
                total += rmax - height[r]
                r-=1

        return total
