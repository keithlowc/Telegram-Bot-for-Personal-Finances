# Telegram-Bot-for-Personal-Finances

Credits to https://github.com/CalicoUFSC for giving the source code.

# Follow these instructions before running the script:
##### 1- Get your Google drive Api key here:
  https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
##### 2- Go to telegram and get your Token from @BotFather
Just message him the following command: `/newbot` and follow the instructions.
##### 3- Fill out the rest of the config.py file

# Usage:

### To install requirements:
`
pip3 install -r requirements.txt
`

### To run with Virtual-environment:

`source fin-bot/bin/activate`

`python3 tesseract_bot.py`

### To run verbose mode (Debug mode)
`
python3 tesseract_bot.py -v
`

### To run normally:
`
python3 tesseract_bot.py
`

### Commands:
Send these commands to your bot:
1. `/start` Displays instruction text
2. `/delete` Deletes latest uploaded value
3. `/total` Displays total value of all receipts
4. `/manual <DIGITS> <THING>` Will manually input the Digits and save the Thing

### Google Sheet example:

![image](https://user-images.githubusercontent.com/25104394/40214652-f3f36c48-5a29-11e8-828b-6b76a34ecb78.png)


### Notes:

1. When taking the picture of the receipt make sure to crop over the price as clean as possible, to avoid any problems with OCR.
2. To stop the script `pkill -f tesseract_bot.py`
3. May exceed Googles Developer Console quota after a long usage

