import camelot
import os
import glob
import pandas as pd

def pdf_to_mult_csv(year, pages):
	
	file = f"bilans_{year}.pdf"
	tables = camelot.read_pdf(file, pages, flavor='lattice')
	nr = 0
	while nr < tables.n:
		if tables[nr].df.columns.stop == 7:
			tables[nr].to_csv(f"{file}_{nr}.csv", index=False)
		nr += 1

def combine_csv(file):
	extension = 'csv'
	all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
	#combine all files in the list
	combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
	#export to csv
	combined_csv.to_csv( f"{file}.csv", index=False, encoding='utf-8-sig')

years = [2018, 2019, 2020, 2021] 

for year in years:
	pdf_to_mult_csv(year,'all')
	combine_csv(f"bilans_{year}")
	
