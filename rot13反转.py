str = "83 89 78 84 45 86 96 45 115 121 110 116 136 132 132 132 108 128 117 118 134 110 123 111 110 127 108 112 124 122 108 118 128 108 131 114 127 134 108 116 124 124 113 108 76 76 76 76 138 23 90 81 66 71 64 69 114 65 112 64 66 63 69 61 70 114 62 66 61 62 69 67 70 63 61 110 110 112 64 68 62 70 61 112 111 112"
list = str.split(" ")
'''
lt = [int(i) for i in list]
print(lt)
'''

lt = []

for i in list:
    lt.append(int(i)-13)
print(lt)

for i in lt:
    print(chr(i),end = "")


'''

lt = map(int,list)
print()
'''
    
'''

lt = [list]
for i in list:
    lt.append(chr(int(i)))
print (lt)
for i in list:
    print(chr(int(i)),end='')
'''
