import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import config 

'''
Created by Keithlowc
Connects to gdrive sheets
'''

date = str(time.strftime("%d/%m/%Y"))

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
	         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(config.GDRIVE_CRED, scope)
client = gspread.authorize(creds)
	 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open(config.GDRIVE_SHEET_NAME).sheet1
	 
def update_sheet(digits,text):
	for i in range(config.GDRIVE_RANGE_OF_CELLS):
		row = i + 1
		col = 1 
		if not sheet.row_values(row, value_render_option='FORMATTED_VALUE'):
			sheet.update_cell(row,col,digits)             #Updates digits
			sheet.update_cell(int(row),int(col + 1),text) #Updates text
			sheet.update_cell(int(row),int(col + 2),date) #Updates date
			return
		else:
			print("\nDATA WAS FOUND ON THIS CELL, SKIPPING TO THE NEXT\n")

def total_spent(row,col): 
	total = str(sheet.cell(row,col).value) 
	return total

def delete_latest():
	for i in range(config.GDRIVE_RANGE_OF_CELLS):
		total = i + 1
		if not sheet.row_values(total, value_render_option='FORMATTED_VALUE'):
			total = total - 1 #Gets last position
			last_val = sheet.cell(total,1).value #Saves last value to display
			sheet.update_cell(total,1,'') #Updates digits
			sheet.update_cell(total,2,'') #Updates text
			sheet.update_cell(total,3,'') #updates date
			return last_val
	
def search_number_string(String):
    index_list = []
    del index_list[:]
    for i, x in enumerate(String):
        if x.isdigit() == True:
            index_list.append(i)
    start = index_list[0]
    end = index_list[-1] + 1
    number = String[start:end]
    return number

