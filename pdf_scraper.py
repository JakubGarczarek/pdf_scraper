import tabula as tb

file = 'http://geoportal.pgi.gov.pl/css/surowce/images/2020/bilans_2020.pdf'
# file = 'bilans_2020.pdf' #do testów lokalnych

df = tb.read_pdf(file, pages = '170-175')
print(df[0])
# tylko konkretne kolumny:
# print(df[0][df.columns.get_loc('Nazwa złoża')]) 
# print(df[0]['Wydo-\rbycie'])

