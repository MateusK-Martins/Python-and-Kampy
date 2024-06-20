
class csv:
    red = '\x1b[41m'
    green = '\x1b[42m'
    yellow = '\x1b[43m'
    blue = '\x1b[44m'
    magenta = '\x1b[45m'
    cyan = '\x1b[46m'
    white = '\x1b[47m'
    close = '\x1b[m'
    def color(t, a):
        return f'{a}{t}{csv.close}'
    
    def treatment(arq='kap.csv', cut=['\n']):
        with open(arq, 'a') as file:
            pass
        with open(arq, 'r') as file:
            arqlist = file.readlines()
        for couty,row in enumerate(arqlist):
            row = row.split(',')
            for xr,i in enumerate(row):
                for countx, i in enumerate(cut):
                    row[xr] = row[xr].replace(cut[countx], '')
            arqlist[couty] = row
        return arqlist
    
    def get_item(arq, y=0,x=0):
        item = []
        try:
            item = arq[y][x]
        except IndexError:
            print('You chosed a invalid number/number out Index of list')
        return item
    
    def num_column(arq):
        return len(arq[0])
    
    def get_column(arq, num=0):
        column = []
        for row in arq:
            try:
                column.append(row[num]) 
            except:
                column.append('None')
        return column
    
    def get_line(arq, y):
        line = []
        try:
            line = arq[y]
        except IndexError:
            print('You chosed a invalid number/number out Index of lines.')
        return line
    
    def get_zone(arq, y=0, x=0, y2=0, x2=0):
        zone = []
        columns = []
        
        for n in range(x, x2 + 1):
            columns.append(csv.get_column(arq, n))
        
        for row_index in range(y, y2 + 1):
            line = []
            for col_index in range(x2 - x + 1):
                if row_index < len(columns[col_index]):
                    line.append(columns[col_index][row_index])
                else:
                    line.append(None)
            zone.append(line)
        return zone
    def printli(arq):
        for county,l in enumerate(arq):
            for countx,i in enumerate(arq):
                if countx != len(arq[0]):
                    print(f'{20*' '^i}', end='')
                else:
                    print(f'{20*' '^i}', end='\n')