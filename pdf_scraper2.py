import camelot
import os
import glob
import pandas as pd


year = 2021

pages = 'all'

file = f"bilans_{year}.pdf"
tables = camelot.read_pdf(file, pages)

# # tables.export('bilans_2021.csv', f='csv')

nr = 0

while nr < tables.n:
	if tables[nr].df.columns.stop == 7:
		tables[nr].to_csv(f"{file}_{nr}.csv", index=False)
		nr += 1
	
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( f"{file}.csv", index=False, encoding='utf-8-sig')