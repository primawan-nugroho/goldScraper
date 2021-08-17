'''
TODO:
Test schedule run in Heroku
[worker.1]: Traceback (most recent call last):
[worker.1]:   File "/app/main.py", line 37, in <module>
[worker.1]:     main()
[worker.1]:   File "/app/main.py", line 33, in main
[worker.1]:     schedule.run_pending()
[worker.1]:   File "/app/.heroku/python/lib/python3.9/site-packages/schedule/__init__.py", line 780, in run_pending
[worker.1]:     default_scheduler.run_pending()
[worker.1]:   File "/app/.heroku/python/lib/python3.9/site-packages/schedule/__init__.py", line 100, in run_pending
[worker.1]:     self._run_job(job)
[worker.1]:   File "/app/.heroku/python/lib/python3.9/site-packages/schedule/__init__.py", line 172, in _run_job
[worker.1]:     ret = job.run()
[worker.1]:   File "/app/.heroku/python/lib/python3.9/site-packages/schedule/__init__.py", line 661, in run
[worker.1]:     ret = self.job_func()
[worker.1]:   File "/app/main.py", line 14, in perform
[worker.1]:     antamLM = goldScraper.getAntamLM()
[worker.1]:   File "/app/goldScraper.py", line 13, in getAntamLM
[worker.1]:     ans = soup.find("td", text="1 gr").find_next_sibling("td").text
[worker.1]: AttributeError: 'NoneType' object has no attribute 'find_next_sibling'
2021-08-16T06:00:05.706374+00:00 heroku[worker.1]: Process exited with status 1
'''
# git remote set-url origin https://github.com/primawan-nugroho/goldScraper.git
from instabot import bot
import goldScraper
from datetime import date
import generateImage
import config
import schedule
import time

TIME = "21:48"

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
    config.postIG(bot, "Post {}.jpg".format(today))
    print("proses image upload")

    print("next schedule : {} {}".format(today,TIME))

def main():
    schedule.every().day.at(TIME).do(perform)
    while True:
        #current_time = datetime.now().strftime("%H:%M:%S")
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()