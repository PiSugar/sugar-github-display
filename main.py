import spidev as SPI
import ST7789
import time

from PIL import Image, ImageDraw, ImageFont, ImageColor
import sys
import urllib.request
import re

# BASE_URL = "https://github.com/LLK/scratch-gui"

BASE_URL = sys.argv[1]

req = urllib.request.Request(BASE_URL)
html = urllib.request.urlopen(req)
doc = html.read().decode('utf8')

STAR_PATTERN = 'starred this repository">\n(.*)\n'
WATCH_PATTERN = 'watching this repository">\n(.*)\n'
FOLK_PATTERN = 'forked this repository">\n(.*)\n'
NAME_PATTERN = '<title>GitHub - (.*):'

star = list(set(re.findall(STAR_PATTERN, doc)))
star = star[0].strip()

watch = list(set(re.findall(WATCH_PATTERN, doc)))
watch = watch[0].strip()

folk = list(set(re.findall(FOLK_PATTERN, doc)))
folk = folk[0].strip()

name = list(set(re.findall(NAME_PATTERN, doc)))
name = name[0].strip()


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

font = ImageFont.truetype("Verdana.ttf", 30)
font2 = ImageFont.truetype("Verdana.ttf", 18)

image = Image.open('template.jpg')
draw = ImageDraw.Draw(image)


draw.text((70, 100), watch, fill = (0,233,255), font = font)
draw.text((70, 145), star , fill = (0,233,255), font = font)
draw.text((70, 190), folk , fill = (0,233,255), font = font)

text_size = draw.textsize(name, font2)
width, height = text_size
print(name)
draw.text(((240-width)/2, 60), name , fill = (0,233,255), font = font2)


disp.ShowImage(image,0,0)
