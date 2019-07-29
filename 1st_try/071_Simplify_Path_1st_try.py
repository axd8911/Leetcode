'''
99.87%
'''


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        
        stock = []
        
        path = [item for item in path if item != '' and item != '.']
        
        for item in path:
            if item != '..':
                stock.append(item)
            elif item == '..' and stock != []:
                stock.pop()
        
        
        
        return '/'+'/'.join(stock)
