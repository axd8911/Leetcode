class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        num = ''
        if str[0] in '-+':
            num = str[0]
            str = str[1:]
        for curr in str:
            if curr.isdigit():
                num+=curr
            else:
                break
        if num in '+-':
            return 0
        output = int(num)
        if output.bit_length()>=32:
            return 2**31-1 if output > 0 else -2**31
        return output
