import goldScraper
from datetime import date
import generateImage
import config

def main():
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
    config.postIG("Post {}.jpg".format(today))
    
if __name__ == "__main__":
    main()