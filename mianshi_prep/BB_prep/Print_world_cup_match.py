# Q2 World cup, M teams, print each round of the match （10min）
# [t1, t2, t3, t4]
# round1: t1 - t2, t3 - t4
# round2: t1 - t3, t2 - t4,
# round3: t1 - t4, t2 - t3
class Solution:
    def match(self,teams):
        output = []
        def helper(combine,idx):
            if combine:
                output.append(combine)
            if idx >= 4:
                return

            m1 = teams[0]+teams[idx]
            m2 = ''.join(teams[1:idx]+teams[idx+1:])
            helper([m1,m2],idx+1)
        helper([],1)
        return output

    def match2(self,teams):
        output = []
        for i in range(len(teams)-1,0,-1):
            m1 = teams[0]+teams[i]
            m2 = ''.join(teams[1:i]+teams[i+1:])
            output.append([m1,m2])
        return output

def main():
    teams = ['Spain','China','USA','Italy']
    a = Solution().match2(teams)
    print (a)

main()
