class Solution:
    def intToRoman(self, num: int) -> str:
        one = ['I','X','C','M']
        five = ['V','L','D']

        position = 0
        res = ''

        while num:
            temp = num%10
            num//=10
            if 0<=temp<=3:
                curr = one[position] * temp

            elif temp == 4:
                curr = one[position] + five[position]

            elif 5<=temp<=8:
                curr = five[position] + one[position] * (temp-5)

            else:
                curr = one[position] + one[position + 1]

            position += 1
            res = curr+res
            print (temp,res)

        return res
