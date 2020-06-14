
sentence = "Ahli Coding Programming Course"
print('Initial: ',sentence)

words = sentence.split(' ')
print(words[2])


def reversechar(word):
    c= 0
    l = len(word)
    nword = []
    for c in range(c,l):
        last = l - 1
        nword.append(word[last-c])
    return ''.join(nword)



print('--------')
last = len(words) - 1
c = 0
result = []
for c in range(c,len(words)):
    # print(words[last-c])
    resword = reversechar(words[last-c])
    result.append(resword)

print(' '.join(result))


arr = ['One','Two','Three']
print(('+').join(arr))





