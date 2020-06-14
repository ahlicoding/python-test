
def processdot(dots,line):
    #erase spacing
    dots = dots.replace('   ','')
    arrdots = []
    i = 0
    #tambahkan 0 di sisi kiri dan kanan ==> 0 1 0  ,  0 1 1 0  ,  0 1 2 1 0  , dsb...
    dots = '0'+dots+'0'
    #print(dots)
    for i in range (i,line):
        #bilangan yang dibawahnya MERUPAKAN penjumlahan bilangan yang di atasnya 2 = 1 + 1
        sum = int(dots[i]) + int(dots[i+1])
        arrdots.append(str(sum)+'   ')

    arrdots = ''.join(arrdots)
    return arrdots


dots = '1' #bilangan teratas
toline = 5
for i in range (1,toline+1):
    dots = processdot(dots,i)
    #insert spacing
    space = ('  '*(toline-i) ) + dots  #kasih jarak, geser ke kanan
    print(space)