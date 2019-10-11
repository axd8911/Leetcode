# does the code pass test cases?
# is the code easily understandable?
# could a different developer revisit the code in 6 months and easily add a new feature? maintainable?

import collections
def solution(songs,song,myLoc):
    length = len(songs)
    songDic = collections.defaultdict(list)
    for i in range(length):
        songDic[songs[i]].append(i)

    mySong = songDic[song]
    searching = [abs(myLoc - (item-length)) for item in mySong] + [abs(myLoc-item) for item in mySong] + [abs(myLoc-(item+length)) for item in mySong]
    print (songDic)
    print (mySong)
    print (searching)
    return min(searching)


songs = ['a','b','d','f','a','c','e','h','b']
print (solution(songs,'a',7))

"""
print
"""
