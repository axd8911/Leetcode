import collections
class Solution:
    def texiCo(self,input):
        # output is the balance for texico and driver
        # API: balance for the platform, destination account
        # BAL: return current balance
        # fee: 2.9% + 0.3
        
        # for the API spliter:
        # get all values
        # if destination: minus the amount 
        
        def APItool(item):
            data = item[item.index(' ')+1:]
            data = data.split('&')
            d_account = None
            d_amount = 0
            for catg in data:
                if catg.startswith('amount'):
                    amount = int(catg[7:])*(1-0.029)-30
                elif catg.startswith('merchant'):
                    account = catg[9:]
                elif catg.startswith('destination'):
                    if 'account' in catg:
                        d_account = catg[21:]                        
                    elif 'amount' in catg:
                        d_amount = int(catg[20:])
                        amount -= d_amount
            return account,amount,d_account,d_amount
            
        dic = collections.defaultdict(int)
        output = []
        for item in input:
            if item.startswith('API'):
                account,amount,d_account,d_amount = APItool(item)
                print (account,amount,d_account,d_amount)
                dic[account] += amount
                if d_account:
                    dic[d_account] += d_amount
            elif item.startswith('BAL'):
                id = item[item.index('=')+1:]
                output.append(round(dic[id]))
            print (dic)
        return output
        
def main():
    input = ['API: amount=1000&merchant=123456789&destination[account]=111111&destination[amount]=877','API: amount=800&merchant=123456789&destination[account]=112211&destination[amount]=622','BAL: merchant=123456789', 'BAL: merchant=112211', 'BAL: merchant=111111']
    input2 = ['API: amount=2000&merchant=10101010','BAL: merchant=10101010']
    input3 = ['API: amount=1000&merchant=123456789&destination[account]=111111&destination[amount]=877','BAL: merchant=123456789','BAL: merchant=111111']
    result = Solution().texiCo(input3)
    print (result)
    
main()
    
                
                    
            
            