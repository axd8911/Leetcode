def solution(words,valid):

    output = []
    for word in words:
        possible = True
        for letter in word:
            if letter.isalpha() and letter.lower() not in valid:
                possible = False
                break
        if possible:
            output.append(word)

    return output

a = ['Hello**','my','dear ','friend!']
b = ['h','e','l','o','m','d','a','r']

print (solution(a,b))
