class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(n):
            output.append('')
            rem1,rem2 = (i+1)%3, (i+1)%5

            if not rem1:
                output[-1] += 'Fizz'
            if  not rem2:
                output[-1] += 'Buzz'
            if not output[-1]:
                output[-1] += str(i+1)
        return output
