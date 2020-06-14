

word = "ahlicoding"
print('initial: ',word)


print(len(word))
c= 0
l = len(word)
nword = []
for c in range(c,l):
    last = l - 1
    nword.append(word[last-c])

print (nword)

#implode in Python
print('result: ',''.join(nword))

#explode in Pythone
