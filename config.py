from instabot import Bot
from datetime import date
import os
import shutil

def postIG(file):
    today = date.today().strftime('%d-%B-%Y')
    bot = Bot()
    bot.login(username = os.getenv("WHOAREYOU"),
              password = os.getenv("IAMYOU"))
    bot.upload_photo(file,
               caption = "Harga emas hari ini {}".format(today))
    bot.logout()

def clean_up():
    today = date.today().strftime('%d-%B-%Y')
    dir = "config"
    img = "Post {}.jpg.REMOVE_ME".format(today)

    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it because in 2021 it makes problems with new uploads
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    # checking whether REMOVE_ME file exists or not
    if os.path.exists(img):
        try:
            # removing it because in 2021 it makes problems with new uploads
            os.remove(img)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))