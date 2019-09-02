# a list of letters, delete if there are three or more same letters in sequence
class Solution:
    def oneD(self,letters):
        stack = []
        for i in range(len(letters)):
            stack.append(letters[i])
            if i<len(letters)-1 and letters[i]!=letters[i+1]:
                n = len(stack)-1
                while n>0:
                    if stack[n] != stack[n-1]:
                        break
                    else:n -= 1
                if len(stack)-1 - n >=2:
                    del stack[n:]
        return ''.join(stack)

def main():
    letters = 'abbbccxxxccadd'
    output = Solution().oneD(letters)
    print (output)

main()
