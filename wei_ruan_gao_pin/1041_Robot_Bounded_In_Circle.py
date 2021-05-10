class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        currDirection = 'N'
        steps = collections.defaultdict(int)
        
        for item in instructions:
            if (item == 'L' and currDirection == 'N') or (item == 'R' and currDirection == 'S'):
                currDirection = 'W'
            elif (item == 'L' and currDirection == 'S') or (item == 'R' and currDirection == 'N'):
                currDirection = 'E'
            elif (item == 'L' and currDirection == 'W') or (item == 'R' and currDirection == 'E'):
                currDirection = 'S'
            elif (item == 'L' and currDirection == 'E') or (item == 'R' and currDirection == 'W'):
                currDirection = 'N'
                
            elif item == 'G':
                steps[currDirection] += 1
        
        if currDirection == 'N' and (steps['W']-steps['E']!=0 or steps['N'] - steps['S']!=0):
            return False
        return True
