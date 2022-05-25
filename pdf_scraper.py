import tabula as tb

file = 'http://geoportal.pgi.gov.pl/css/surowce/images/2020/bilans_2020.pdf'
# file = 'bilans_2020.pdf' #do testów lokalnych

df = tb.read_pdf(file, pages = '162-406')#zakres stron w bilansie dla  piasków i żwirów

piaski_zwiry = {}
page = 0
while (page <= 2):#liczba stron z podanego zakresu do skrapowania
    for index, row in df[page].iterrows():
        piaski_zwiry[row[2]]=[row[3],row[4], row[5], row[6], row[7]]
    page += 1
        
print(piaski_zwiry)

f = open('piaski_zwiry.txt','w')
f.write(str(piaski_zwiry))
f.close()






