#######################  Telegram Bot Config #######################

BOT_TOKEN='<BOT TOKEN>' # the token you get from botfather
CACHE_DIR='<DIR/TO/PROJECT>' # the directory used to store received images
CACHE_TEMP=True # if True, images on cache will be deleted after parsing 

####################################################################


#######################  Google Drive Config #######################
'''
NOTE: MAKE SURE TO SHARE THE GOOGLE SHEET WITH THE client_email IN THE JSON FILE
OTHERWISE THE CODE WILL NOT WORK
'''
GDRIVE_CRED='client.json' #This is the name of the file you download from the console.developers.google.com/apis
						  #Make sure to change the name of the downloaded file to client.json or whatever you like
GDRIVE_SHEET_NAME='<NAME OF THE SHEET>' #Name of the excel sheet on your drive
GDRIVE_A1_CELL_TEXT='Amount:' #Text that goes on cell A1 ie: Amount: this will stop from deleting that row 
GDRIVE_RANGE_OF_CELLS=1000 #number of cells you will be uploading values to recommended 1000

####################################################################


