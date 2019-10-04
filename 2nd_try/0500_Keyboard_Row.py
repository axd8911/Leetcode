class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {'q':0,'w':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,'a':1,'s':1,'d':1,'f':1,'g':1,'h':1,'j':1,'k':1,'l':1,'z':2,'x':2,'c':2,'v':2,'b':2,'m':2,'n':2}

        def match(myStr):
            for i in range(1,len(myStr)):
                if dic[myStr[i].lower()] != dic[myStr[i-1].lower()]:
                    return False
            return True


        output = []
        for word in words:
            if match(word):
                output.append(word)

        return output
