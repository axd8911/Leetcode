def test(minput):

    dic = {}

    def spliter(item):
        print (item)
        idx = item.index(' ')
        data = item[idx+1:]
        data = data.split('&')
        # print (data)
        valid = False
        for catg in data:
            if catg.startswith('id'):
                id = int(catg[3:])
            elif catg.startswith('amount'):
                amount = int(catg[7:])
            elif catg.startswith('currency'):
                # print ('yes',catg[9:],data,catg[9:] == 'USD')
                valid = catg[9:] == 'USD'
        action = item[:idx-1]
        # print(action,id,amount,valid)
        return action, id, amount, valid
        
    for item in minput:
        action, id, amount, valid = spliter(item)
        # print (action, id, amount, valid)
        if not valid:
            continue
        if action == 'CREATE':
            dic[id] = amount
        elif action == 'FINALIZE':
            try:
                dic.pop(id)
            except:
                continue
            else:
                dic[id] = amount
        elif action == 'PAY':
            del dic[id]
    # print (dic)
    return sum(dic.values())


def main():
    minput = ['CREATE: id=13&currency=USD&amount=800','FINALIZE: id=13&amount=300&currency=USD','CREATE: id=14&amount=800&currency=USD&memo=home work','PAY: id=14&amount=800&currency=USD&memo=home work','FINALIZE: id=15&amount=300&currency=USD']

    print(test(minput))

main()
