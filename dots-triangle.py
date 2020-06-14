# print('   A ')
# print('  B C')
# print(' D E F')
# print('G H I J')

# for i in range(1,10):
#     print('Line: ',i)

toline = int(input('Input How many Line:'))
for i in range (1,toline+1):
    dots = ('*' + ' ')*i
    space = (' '*(toline-i) ) + dots
    print(space)



