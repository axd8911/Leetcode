'''
Leetcode score: 80.47%
Memory: 5.79% , still slightly slower than most.

Comments:
1. some_strings.replace('original','something you want')
2. efficiency: it is helpful to remove + first in order to drop some items


'''


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        maillist = []
        for email in emails:
            email = email.split('@')
            email[0] = email[0].split('+')
            email[0] = email[0][0]
            email[0] = email[0].replace('.','')
            email = email[0] + '@' + email[1]
            
            if email not in maillist:
                maillist.append(email)



        return len(maillist)
