import spidev as SPI
import ST7789
import time

from PIL import Image, ImageDraw, ImageFont, ImageColor
import sys
import urllib.request
import re
import time

# Regx
STAR_PATTERN = 'starred this repository">\n(.*)\n'
WATCH_PATTERN = 'watching this repository">\n(.*)\n'
FOLK_PATTERN = 'forked this repository">\n(.*)\n'
NAME_PATTERN = '<title>GitHub - (.*):'

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 24
bus = 0 
device = 0 

# 240x240 display with hardware SPI:
disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)

# Initialize library.
disp.Init()

# Launch Screen
logo = Image.open('pisugar.jpg')
launch = ImageDraw.Draw(logo)
disp.ShowImage(logo,0,0)

BASE_URL = sys.argv[1]

timer = 0
interval  = 100
star = ""
folk = ""
watch = ""
name = ""

font = ImageFont.truetype("Verdana.ttf", 30)
font2 = ImageFont.truetype("Verdana.ttf", 18)

## render loop
while(True):

    # draw background
    image = Image.open('template.jpg')
    draw = ImageDraw.Draw(image)

    # send request
    if timer % interval == 0:
        req = urllib.request.Request(BASE_URL)
        html = urllib.request.urlopen(req)
        doc = html.read().decode('utf8')

        starList = list(set(re.findall(STAR_PATTERN, doc)))
        star = starList[0].strip()

        watchList = list(set(re.findall(WATCH_PATTERN, doc)))
        watch = watchList[0].strip()

        folkList = list(set(re.findall(FOLK_PATTERN, doc)))
        folk = folkList[0].strip()

        nameList = list(set(re.findall(NAME_PATTERN, doc)))
        name = nameList[0].strip()

        print("Get project data: " + name)

    # draw numbers
    draw.text((70, 100), watch, fill=(0, 233, 255), font=font)
    draw.text((70, 145), star, fill=(0, 233, 255), font=font)
    draw.text((70, 190), folk, fill=(0, 233, 255), font=font)

    # draw project name
    text_size = draw.textsize(name, font2)
    width, height = text_size
    draw.text(((240 - width) / 2, 60), name, fill=(0, 233, 255), font=font2)

    # draw counter
    draw.rectangle([(0, 2), (240 * (timer % interval) / interval, 2)], fill="RED")

    # render
    disp.ShowImage(image,0,0)

    time.sleep(0.01)
    timer+=1
