from instabot import Bot
from datetime import date
import os
import shutil
import time

def postIG(bot, file):
    bot = Bot()
    time.sleep(5)
    bot.login(username = os.getenv("WHOAREYOU"),
              password = os.getenv("IAMYOU"), is_threaded = False)

    today = date.today().strftime('%d-%B-%Y')
    time.sleep(1)
    bot.upload_photo(file,
               caption = "Harga emas hari ini {}".format(today))
    time.sleep(1)
    bot.logout()

def clean_up():
    # check folder config dan file REMOVE_ME exist atau tidak
    # kalo exist, hapus!!
    # bug di instabot gabisa upload kalo ada 2 file/folder diatas
    today = date.today().strftime('%d-%B-%Y')
    dir = "config"
    img = "Post.jpg.REMOVE_ME"

    if os.path.exists(dir):
        try:
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(img):
        try:
            os.remove(img)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))