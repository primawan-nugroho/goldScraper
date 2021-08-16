from instabot import bot
import goldScraper
from datetime import date, datetime
import generateImage
import config
import schedule
import time

TIME = "13:00"

def perform():
    today = date.today().strftime('%d-%B-%Y')    

    antamLM = goldScraper.getAntamLM()
    antamIndoGold = goldScraper.getAntamIndoGold()
    UBS = goldScraper.getUBSIndoGold()

    print(date.today())
    print("Antam Logam Mulia : Rp {}".format(antamLM))
    print("Antam Indo Gold : Rp {}". format(antamIndoGold))
    print("UBS Indo Gold : Rp {}". format(UBS))

    generateImage.drawPrice(antamIndoGold, UBS, antamLM)
    config.clean_up()    
    config.postIG(bot,"Post {}.jpg".format(today))

def main():
    schedule.every().day.at(TIME).do(perform)
    while True:
        today = date.today().strftime('%d-%B-%Y')    
        #current_time = datetime.now().strftime("%H:%M:%S") 
        print("scheduled : {} {}".format(today, TIME))
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()