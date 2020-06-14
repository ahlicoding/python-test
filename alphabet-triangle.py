
mystring= 'ABCDEFGHIJKLM'


def extract(mylist,line):
    sarr = []
    i = 0
    for i in range(i,line):
        if i <= int(line):
            sarr.append(mylist[i])
    return ''.join(sarr)

def makespace(mystring):
    i = 0
    arr = []
    for i in range (i,len(mystring)):
        arr.append(mystring[i]+' ')
    arr = ''.join(arr)
    return arr


line = []
i = 1
arrambil = []
while len(mystring) >= 1 :

    # Cari cara memecah Array menjadi array yg lebih kecil
    if len(mystring) >= i:
        ambil = extract(mystring,i)
        line.append(extract(mystring,i))
        mystring = mystring[len(ambil):len(mystring)]
    else:
        dif = i-len(mystring)
        ambil = mystring + ('-'*dif)
        mystring = ''
   # print('Ambil:',ambil,' , ',mystring)
    arrambil.append(ambil)
    i = i+1

print(arrambil)



toline = i
last = toline - 1
for i in range (1,toline):
    dots =  makespace(arrambil[i-1])+' '*i
    space = (' '*(last-i) ) + dots
    print(space)

