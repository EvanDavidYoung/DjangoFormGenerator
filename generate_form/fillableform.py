import os 
import pypdftk as py




def generate_form(datas):
	PATH = 'SOFC-Credit-Card-Payment.pdf'
	var = py.dump_data_fields('SOFC-Credit-Card-Payment.pdf')
	for elem in var:
		print(elem['FieldName'])
	datas = {
		'Account Number': '12345',
		'Contact': 'Evan'
	}
	generated_pdf = py.fill_form(PATH, datas, out_file = 'new_pdf.pdf')
	print('form has been generated')