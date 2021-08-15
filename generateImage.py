# importing image object from PIL
import math
from PIL import Image, ImageDraw, ImageFont
import datetime

def drawPrice(antamIndogoldPrice, UBSIndogoldPrice, antamLMPrice):
    W = 1600
    today = datetime.date.today().strftime('%d-%B-%Y')
    img = Image.open(r'D:\Python\goldScraper\Resources\blank_design.jpg')
    canvas = ImageDraw.Draw(img)

    # draw today in center alignment
    font = ImageFont.truetype(r'D:\Python\goldScraper\Resources\Poppins\Poppins-SemiBold.ttf', 70)
    text_width, text_height = canvas.textsize(today, font)
    position = ((W-text_width)/2, 193)
    canvas.text(position, today, (255,255,255),font=font)

    font = ImageFont.truetype(r'D:\Python\goldScraper\Resources\Poppins\Poppins-SemiBold.ttf', 100)

    # draw harga antam indogold
    canvas.text((780, 490), antamIndogoldPrice,(255,255,255),font=font)

    # draw harga UBS indogold
    canvas.text((780, 780),UBSIndogoldPrice,(255,255,255),font=font)

    # draw harga Antam Logam Mulia
    canvas.text((780, 1250),antamLMPrice,(255,255,255),font=font)

    # draw gram
    font = ImageFont.truetype(r'D:\Python\goldScraper\Resources\Poppins\Poppins-Medium.ttf', 50)
    canvas.text((1200, 550),"/gr",(255,255,255),font=font)
    canvas.text((1200, 840),"/gr",(255,255,255),font=font)
    canvas.text((1200, 1310),"/gr",(255,255,255),font=font)

    #img.show()
    img.save("Post {}.jpg".format(today))