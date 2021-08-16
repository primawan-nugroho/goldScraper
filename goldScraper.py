from bs4 import BeautifulSoup as BS
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

def getAntamLM():
    url = "https://www.logammulia.com/id/harga-emas-hari-ini"
    data = requests.get(url, headers = headers)
    soup = BS(data.text, 'html.parser')
    #print(soup.prettify())
    ans = soup.find("td", text="1 gr").find_next_sibling("td").text
    return ans

def getAntamIndoGold():
    url = "https://www.indogold.id/harga-emas-hari-ini"
    data = requests.get(url, headers = headers)
    soup = BS(data.text, 'html.parser')
    #print(soup.prettify())

    #get html file under tab1 (Antam)
    ans = soup.find("div", id="tab1")
    
    #2nd html parsing
    soup = BS(ans.text, 'html.parser')

    #find price for 1.0 gram
    ans2 = ans.find("td", text="1.0 gram").find_next_sibling("td").text #find
    return ans2.split("Rp ")[1]

def getUBSIndoGold():
    url = "https://www.indogold.id/harga-emas-hari-ini"
    data = requests.get(url, headers = headers)
    soup = BS(data.text, 'html.parser')
    #print(soup.prettify())

    #get html file under tab0 (UBS Gold)
    ans = soup.find("div", id="tab0")
    
    #2nd html parsing
    soup = BS(ans.text, 'html.parser')

    #find price for 1.0 gram
    ans2 = ans.find("td", text="1.0 gram").find_next_sibling("td").text #find
    return ans2.split("Rp ")[1]
