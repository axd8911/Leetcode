class Solution:
    def compress(self, chars: List[str]) -> int:
        order = 0
        curr = 0
        for i in range(len(chars)):
            if i == 0:
                curr = 1
                order+=1
            else:
                if chars[i] == chars[i-1]:
                    curr += 1
                else:
                    if curr > 1:
                        for digit in str(curr):
                            chars[order]=digit
                            order += 1
                    curr = 1
                    chars[order]=chars[i]
                    order+=1
                if i == len(chars)-1:
                    if curr > 1:
                        for digit in str(curr):
                            chars[order]=digit
                            order += 1
        return order
