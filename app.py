from kampy.csv import kampy

cut = ['\r', '\t', '\n']
kampy.settings(cut)

arq = kampy.cinl('kap.csv')
arq = kampy.clean(arq)

kampy.clear()

arq = kampy.get_column(arq,2)

kampy.printli(arq, 'column')

#ATENÇÃo Nomes e informações do arquivo csv foram gerados aleatóriamente