class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {0:'',1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        
        factor = 1000
        res = []
        while factor>0:
            current = num//factor
            if current<=3:
                res += [factor] * current
            
            elif current ==4:
                res += [factor, factor*5]
                
            elif 5<=current <=8:
                res += [factor*5]+[factor]*(current-5)
                
            elif current==9:
                res+=[factor,factor*10]
            
            num = num%factor
            factor //=10
        return ''.join([dic[item] for item in res])
