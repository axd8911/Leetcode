# eight hex digits


class Solution:
    def accountNumberValidation(self,account):
        part1 = account[:2]
        part2 = account[2:]
        dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        multiplier = 16**5
        total = 0
        for item in part2:
            if item.isdigit():
                total += int(item)*multiplier
            else:
                total += dic[item.upper()]*multiplier
            multiplier /= 16
            print (item,total)
        print (total)
        summation = 0
        while total:
            curr = total%10
            total//=10
            summation += curr

        output = 0
        for item in part1:
            output *= 16
            if item.upper() in dic:
                output += dic[item.upper()]
            else:
                output += int(item)
        print (summation,output)
        return output == summation


def main():

    number = '21abcdef'
    a = Solution().accountNumberValidation(number)
    print (a)

main()
