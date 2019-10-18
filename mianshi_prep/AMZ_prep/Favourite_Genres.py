import collections
import time
def solution(userSongs, songGenres):
    dic = {}
    for key in songGenres:
        for song in songGenres[key]:
            dic[song] = key

    res = collections.defaultdict(list)
    for key in userSongs:
        count = collections.defaultdict(int)
        for song in userSongs[key]:
            if song in dic:
                count[dic[song]] += 1
        if count:
            most = max(count.values())
            for key2 in count:
                if count[key2] == most:
                    res[key].append(key2)
        else:
            res[key] = []

    return res


def favGenres(userSongs, songGenres):
    output = {}
    for user in userSongs:
        song_list = userSongs[user]
        count = {}

        for song in song_list:
            for genre in songGenres:
                if(song in songGenres[genre]):
                    count[genre] = count.get(genre,0) + 1

        output[user] = [key for key, val in count.items() if val == max(count.values())]

    return output

if __name__ == "__main__":
    userSongs = {"David":["song1", "song2", "song3", "song4", "song8"],
                    "Emma":["song5", "song6", "song7"]}


    songGenres = {"Rock":["song1", "song3"],
                    "Dubstep": ["song7"],
                    "Techno":["song2", "song4"],
                    "Pop":["song5", "song6"],
                    "Jazz":["song8", "song9"]}
    #songGenres = {}
    a = time.time()
    output = favGenres(userSongs, songGenres)
    b = time.time()
    res = solution(userSongs,songGenres)
    c = time.time()
    print (b-a,c-b)
    print (res)
    print (output)
