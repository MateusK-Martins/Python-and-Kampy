import os

class kampy:
    def settings(cut):
        kampy.cut = list(cut)
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
    def cinl(arq):
        try:
            with open(arq, 'a'):
                pass 
            with open(arq, 'r') as file:
                lines = file.readlines()
                arqlist = []
                for row in lines:
                    i = row.split(',')
                    arqlist.append(i)
            return arqlist
        except FileNotFoundError:
            print(f"File {arq} not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    def clean(arq):
        for row in arq:
            for countx, i in enumerate(row):
                for cut in kampy.cut:
                    if i.find(cut) != -1:
                        i = i.replace(cut, '-')
                        row[countx] = i
        for row in arq:
            row[:] = [item for item in row if '-' not in item]
        
        return arq
    def column(arq):
        number_column = 0
        for c in arq[0]:
            number_column += 1
        return number_column
    
    def printli(arq, typei='list'):
        closed = '\033[m'
        if typei == 'list':
            try:
                for county, row in enumerate(arq):
                    if county == 0:
                        cor = '\033[049m'
                    elif county % 2 == 1:
                        cor = '\033[047m'
                    elif county != 0:
                        cor = '\033[042m'
                    
                    for i in row:
                        print(f'{cor}{i:<20}{closed}', end='')
                    print()
            except:
                pass
        elif typei == 'column':
            try:
                for countx, i in enumerate(arq):
                    if countx == 0:
                        cor = '\033[049m'
                    elif countx % 2 == 1:
                        cor = '\033[047m'
                    elif countx != 0:
                        cor = '\033[042m'
                    
                    print(f'{cor}{i:<20}{closed}', end='')
                    print()
            except:
                pass
    def get_line(arq, y):
        line = arq[y]
        return line
    def get_column(arq, x):
        column = []
        for row in arq:
            for countx,i in enumerate(row):
                if countx == x:
                    column.append(i)
                else:
                    pass
        return column
    def get_item(arq, y, x):
        '''
        get_item function needs, the elements: y(line), x(column)
        It needs to get a specific item.
        '''
        try:
            cont = -1
            for row in arq:
                cont += 1
                if cont == y:
                    if x <= len(row):
                        return row[x-1]
        except:
            pass
    def get_zone(arq, y1, x1, y2, x2):
        try:
            zone = []
            for county, row in enumerate(arq):
                if y1 <= county <= y2:
                    line = []
                    for countx, i in enumerate(row):
                        if x1 <= countx <= x2:
                            line.append(i)
                    zone.append(line)
            return zone
        except IndexError as e:
            print(f'Your number informateds is out {e}')
