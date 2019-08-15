class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # an art of deleting: if more (,delete(
        #in order: 0 to idx 1, we need to delete ), 0 to idx2,we need to delete ))
        #reversed: idx4 to idx3, delete (, idx4 to idx2, delete ((
        #save the locations until where we should delete as least a element
        left,right = 0,0
        l_set,r_set = [],[]

        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1
            if left<right:
                l_set.append(i)
                right-=1
        left,right = 0,0
        for j in range(len(s)-1,-1,-1):
            if s[j] == '(':
                left += 1
            elif s[j] == ')':
                right += 1
            if left>right:
                r_set.append(j)
                left-=1

        output = set()
        output.add(s)

        r_set = [item-len(l_set) for item in r_set]

        while l_set:
            idx = l_set.pop(0)
            new = set()
            while output:
                curr = output.pop()
                for i in range(idx+1):
                    if curr[i] == ')':
                        new.add(curr[:i]+curr[i+1:])
            output = new
            l_set = [item-1 for item in l_set]

        while r_set:
            idx = r_set.pop(0)
            new = set()
            while output:
                curr = output.pop()
                for i in range(len(curr)-1,idx-1,-1):
                    if curr[i] == '(':
                        new.add(curr[:i]+curr[i+1:])
            output = new

        if not output:
            return [""]
        return output
