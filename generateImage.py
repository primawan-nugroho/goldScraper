# importing image object from PIL
from PIL import Image, ImageDraw, ImageFont
import datetime
import requests


def drawPrice(antamIndogoldPrice, UBSIndogoldPrice, antamLMPrice):
    url_blankdesign = 'https://github.com/primawan-nugroho/goldScraper/blob/master/Resources/blank_design.jpg?raw=true'
    url_poppins_semibold = 'https://github.com/primawan-nugroho/goldScraper/blob/master/Resources/Poppins/Poppins-SemiBold.ttf?raw=true'
    url_poppins_medium = 'https://github.com/primawan-nugroho/goldScraper/blob/master/Resources/Poppins/Poppins-Medium.ttf?raw=true'
    W = 1600
    today = datetime.date.today().strftime('%d-%B-%Y')
    img = Image.open(requests.get(url_blankdesign, stream=True).raw)
    canvas = ImageDraw.Draw(img)

    # draw today in center alignment
    font = ImageFont.truetype(requests.get(url_poppins_semibold, stream=True).raw, 70)
    text_width, text_height = canvas.textsize(today, font)
    position = ((W-text_width)/2, 193)
    canvas.text(position, today, (255,255,255),font=font)

    font = ImageFont.truetype(requests.get(url_poppins_semibold, stream=True).raw, 100)

    # draw harga antam indogold
    canvas.text((780, 490), antamIndogoldPrice,(255,255,255),font=font)

    # draw harga UBS indogold
    canvas.text((780, 780),UBSIndogoldPrice,(255,255,255),font=font)

    # draw harga Antam Logam Mulia
    canvas.text((780, 1250),antamLMPrice,(255,255,255),font=font)

    # draw gram
    font = ImageFont.truetype(requests.get(url_poppins_medium, stream=True).raw, 50)
    canvas.text((1200, 550),"/gr",(255,255,255),font=font)
    canvas.text((1200, 840),"/gr",(255,255,255),font=font)
    canvas.text((1200, 1310),"/gr",(255,255,255),font=font)

    img.save("Post.jpg", "JPEG")
