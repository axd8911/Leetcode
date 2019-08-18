class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        word_list = []
        space_list = []
        output = []
        n = 0
        while n < len(words):
            rest = maxWidth
            word_list.append([])
            space_list.append([])
            output.append('')
            while True:
                length = len(words[n])
                if rest > length:
                    word_list[-1].append(words[n])
                    space_list[-1].append(1)
                    n+=1
                    rest -= length+1
                elif rest == length:
                    word_list[-1].append(words[n])
                    n+=1
                    break
                else:
                    space_list[-1][-1] += rest
                    if len(space_list[-1])>1:
                        amount = len(space_list[-1])-1
                        each = sum(space_list[-1])//amount
                        extra = sum(space_list[-1])%amount
                        space_list[-1] = [each+1] * extra + [each] * (amount - extra)
                    break
                if n == len(words):
                    space_list[-1][-1] += rest
                    break
            for i in range(len(word_list[-1])):
                output[-1] += word_list[-1][i]
                if i < len(space_list[-1]):
                    output[-1]+= ' ' * space_list[-1][i]
        return output
