class Solution:
    def intToRoman(self, num: int) -> str:

        table = {1:['I','X','C','M'],5:['V','L','D']}
        output = ''
        pw = 3

        while pw >= 0:
            curr = num//10**pw
            if curr == 9:
                output += table[1][pw]+table[1][pw+1]
            elif 5<=curr<=8:
                output += table[5][pw] + table[1][pw]*(curr-5)
            elif curr == 4:
                output += table[1][pw]+table[5][pw]
            elif 0<=curr<=3:
                output += table[1][pw] * curr

            num -= curr*10**pw
            pw-=1

        return output
