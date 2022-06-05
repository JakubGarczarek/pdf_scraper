import tabula as tb
import csv

file = 'http://geoportal.pgi.gov.pl/css/surowce/images/2020/bilans_2020.pdf'
# file = 'bilans_2020.pdf' #do testów lokalnych

df = tb.read_pdf(file,stream=False, pages = '91-500')#sensowny zakres stron w bilansie do skrapowania 
outputFile = open('bilans.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

page = 0

symbol_zag = ['B','E','G','M','P','R','Z','T','K']

while (page < 400):#liczba stron z podanego zakresu do skrapowania
    
    for index, row in df[page].iterrows():
         
            index_kol = 0
            index_zag = 0
            while index_kol < len(row):
                                
                if row[index_kol] in symbol_zag:
                    index_zag = index_kol

                index_kol += 1
            if index_zag > 0:
                try:
                    nazwa_zloza = row[index_zag-1]
                    stan_zag = row[index_zag]
                    zas_geol = row[index_zag+1]
                    zas_przem = row[index_zag+2]
                    wydobycie = row[index_zag+3]
                    if (index_zag + 4) <= len(row):
                        powiat = row[index_zag+4]
                    else:
                        powiat = 'brak_danych'

                    print(nazwa_zloza, stan_zag, zas_geol, zas_przem, wydobycie)
                    outputWriter.writerow([nazwa_zloza, stan_zag, zas_geol, zas_przem, wydobycie, powiat])
                except IndexError:
                    pass
   
    page += 1
    print('=======================STRONA==========================')
            
print(f"Liczba stron: {page}")
outputFile.close()





