#######################  Telegram Bot Config #######################

BOT_TOKEN='<YOUR BOT TOKEN>' # the token you get from botfather
CACHE_DIR='<YOUR/PROJECT/DIRECTORY>' # the directory used to store received images
CACHE_TEMP=True # if True, images on cache will be deleted after parsing 

####################################################################

#######################  Google Drive Config #######################

'''
NOTE: MAKE SURE TO SHARE THE SHEET WITH THE client_email IN THE JSON FILE
OTHERWISE THE CODE WILL NOT WORK
'''

GDRIVE_CRED='client.json' #This is the name of the file you download from the console.developers.google.com/apis
						  #Make sure to change the name of the downloaded file to client.json or whatever you like
GDRIVE_SHEET_NAME='<GOOGLE SHEET FILE NAME>' #Name of the excel sheet on your drive
GDRIVE_RANGE_OF_CELLS=1000 #number of cells you will be uploading values to

####################################################################




