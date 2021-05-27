class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        num1 = [int(item) for item in num1]
        num2 = [int(item) for item in num2]
        output = []
        length = max(len(num1),len(num2))
        carry = 0
        for i in range(length):
            if i>=len(num1):
                curr1 = 0
            else:
                curr1 = num1[i]
            if i>=len(num2):
                curr2 = 0
            else:
                curr2 = num2[i]
            curr = curr1 + curr2 + carry
            output.append(curr%10)
            carry = curr//10
        if carry==1:
            output.append(1)
        output = [str(item) for item in output]
        output = ''.join(output[::-1])
        return output
