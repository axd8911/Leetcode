# two list of strings, a and b. Is all strings in b combined by elements in a?
def solution(a,b):
    allcombine = []
    def bt(wordList, combine):
        allcombine.append(combine)
        for i in range(len(wordList)):
            bt(wordList[:i]+wordList[i+1:],combine+wordList[i])

    bt(a,'')
    print (len(allcombine))
    for item in b:
        if item not in allcombine:
            return False
    return True

if __name__ == "__main__":
    a = ['have','a','great','day']
    b = ['havea','haveaday','hopeyou','hopedaygreat','','agreat','youi']
    print (solution(a,b))
