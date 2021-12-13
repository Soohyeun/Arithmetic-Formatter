
def arithmetic_arranger(num_list, cal=False):

    sp=' '
    das='-'
    a = str()
    b = str()
    c = str()
    d = str()

#Error1
    if len(num_list) > 5:
        print('Error: Too many problems.')
        exit()


#Extract
    for i in range(len(num_list)):
        num_list[i] = num_list[i].split()

    #Error2
        try:
            x = int(num_list[i][0])
            y = int(num_list[i][2])
        except:
            print('Error: Numbers must only contain digits.')
            exit()

    #Error3
        if x >= 10000 or y >= 10000:
            print('Error: Numbers cannot be more than four digits.')
            exit()

    #Calculation
        if num_list[i][1] == '+':
            num_list[i].append(x+y)
            num_list[i][3] = str(num_list[i][3])
        elif num_list[i][1] == '-':
            num_list[i].append(x-y)
            num_list[i][3] = str(num_list[i][3])
    #Error4
        else:
            print('Error: Operator must be \'+\' or \'-\'.')
            exit()

#Print
        if len(num_list[i][0]) >= len(num_list[i][2]):
            a = a + sp*2 + num_list[i][0] + sp*4
            b = b + num_list[i][1] + sp*(len(num_list[i][0])-len(num_list[i][2])+1) + num_list[i][2] + sp*4
            c = c + das*(len(num_list[i][0])+2) + sp*4
            d = d + sp*(2 + len(num_list[i][0]) - len(num_list[i][3])) + num_list[i][3] + sp*4
            
        else:
            a = a + sp*(len(num_list[i][2])-len(num_list[i][0])+2) + num_list[i][0] + sp*4
            b = b + num_list[i][1] + sp + num_list[i][2] + sp*4
            c = c + das*(len(num_list[i][2])+2) + sp*4
            d = d + sp*(2 + len(num_list[i][2]) - len(num_list[i][3])) + num_list[i][3] + sp*4


# Input True or not
    if cal:
        print(a)
        print(b)
        print(c)
        print(d)
    else:
        print(a)
        print(b)
        print(c)
