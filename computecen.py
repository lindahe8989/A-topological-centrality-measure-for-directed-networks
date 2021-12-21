file = open("2007 A-gamma", 'r')
total = 0
print('origin')
for i in file.readlines():
    #print(i)
    if i=='\n':
        continue
    elif 'i=' in i:
        number_i = i.split('=')[1]
        print(total)
        print(i)
        total = 0
        continue
    list_2 = i.split(')')
    #print(list_2[0].split(','))
    try:
        decimal = float(list_2[0].split(',')[1])
        if decimal==float('inf'):
            continue
        total+=decimal
    except:
        print(i)
        print(list_2[0].split(','))
    #print(decimal)
print(total)