import os 
import pypdftk as py

def generate_form(datas):
	module_dir = os.path.dirname(__file__)  # get current directory
	PATH = os.path.join(module_dir, "SOFC-Credit-Card-Payment.pdf")
	var = py.dump_data_fields(PATH)
	for elem in var:
		print(elem['FieldName'])

	generated_pdf = py.fill_form(PATH, datas, out_file = os.path.join(module_dir,'new_pdf.pdf'))
	print('form has been generated')


# datas = dict()
# datas['Account Number'] = 123456
# datas['SubAccount']		= 123456
# datas['Amount'] 		= 123
# # datas['Date'] 			= date
# # datas['Org Name'] 		= org 
# generate_form(datas)


# Account Number
# SubAccount
# Date mmddyyyy
# Amount
# Vendor
# Contact
# Phone
# Reservation Phone
# Reservation Guest
# Reservation by
# Start Date
# End Date
# Statement of Benefit
# Leader Phone
# Leader Date
# Advisor Phone
# Advisor Date
# Travel 1
# Travel 2
# Org Name
# Invoice Confirmation