# -*- coding: utf-8 -*-
"""easyocr

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PPHOrHg0oklSlSV5-oRJ1s7qxiXss7za

Language	Code Name
Abaza	abq
Adyghe	ady
Afrikaans	af
Angika	ang
Arabic	ar
Assamese	as
Avar	ava
Azerbaijani	az
Belarusian	be
Bulgarian	bg
Bihari	bh
Bhojpuri	bho
Bengali	bn
Bosnian	bs
Simplified Chinese	ch_sim
Traditional Chinese	ch_tra
Chechen	che
Czech	cs
Welsh	cy
Danish	da
Dargwa	dar
German	de
English	en
Spanish	es
Estonian	et
Persian (Farsi)	fa
French	fr
Irish	ga
Goan Konkani	gom
Hindi	hi
Croatian	hr
Hungarian	hu
Indonesian	id
Ingush	inh
Icelandic	is
Italian	it
Japanese	ja
Kabardian	kbd
Kannada	kn
Korean	ko
Kurdish	ku
Latin	la
Lak	lbe
Lezghian	lez
Lithuanian	lt
Latvian	lv
Magahi	mah
Maithili	mai
Maori	mi
Mongolian	mn
Marathi	mr
Malay	ms
Maltese	mt
Nepali	ne
Newari	new
Dutch	nl
Norwegian	no
Occitan	oc
Pali	pi
Polish	pl
Portuguese	pt
Romanian	ro
Russian	ru
Serbian (cyrillic)	rs_cyrillic
Serbian (latin)	rs_latin
Nagpuri	sck
Slovak	sk
Slovenian	sl
Albanian	sq
Swedish	sv
Swahili	sw
Tamil	ta
Tabassaran	tab
Telugu	te
Thai	th
Tajik	tjk
Tagalog	tl
Turkish	tr
Uyghur	ug
Ukranian	uk
Urdu	ur
Uzbek	uz
Vietnamese	vi
"""

!pip install easyocr

# load example images
!npx degit JaidedAI/EasyOCR/examples -f

# list them
!ls -l

!wget https://ts-spain.com/wp-content/uploads/2019/02/Starbucks.jpg
!wget https://www.oncos.com.mx/uploads/1/2/4/4/124490058/published/mastograf-a-digital.jpg
!wget https://www.oncos.com.mx/uploads/1/2/4/4/124490058/published/mastografia-posterior-a-trata-miento-por-cancer-de-mama.jpg
!wget https://p4.wallpaperbetter.com/wallpaper/720/556/1009/letters-background-words-i-believe-in-you-wallpaper-preview.jpg
! ls

starbucks='/content/Starbucks.jpg'
mastografia1='/content/mastograf-a-digital.jpg'
mastografia2='/content/mastografia-posterior-a-trata-miento-por-cancer-de-mama.jpg'
ejemplo_believe = '/content/letters-background-words-i-believe-in-you-wallpaper-preview.jpg'

# show an image
import PIL
from PIL import ImageDraw
#im = PIL.Image.open("thai.jpg")
#im

#pruebas
im = PIL.Image.open(starbucks)
#im = PIL.Image.open(mastografia2)
#im = PIL.Image.open(ejemplo_believe)
im

# Create a reader to do OCR.
# If you change to GPU instance, it will be faster. But CPU is enough.
# (by MENU > Runtime > Change runtime type > GPU, then redo from beginning )
import easyocr
#reader = easyocr.Reader(['th','en'])

#pruebas
reader = easyocr.Reader(['en','en'])

# Doing OCR. Get bounding boxes.
#bounds = reader.readtext('thai.jpg')
#bounds
reader = easyocr.Reader(['en'])
#pruebas
bounds = reader.readtext(starbucks)
#bounds = reader.readtext(mastografia2)
#bounds = reader.readtext(ejemplo_believe)
bounds

#reader = easyocr.Reader(['en'])
#reader.readtext('chinese_tra.jpg', detail = 0, paragraph=True)
lector = reader.readtext(starbucks, detail = 0, paragraph=True)
#bounds = reader.readtext(starbucks)
#bounds

lector = reader.readtext(starbucks, detail = 0, paragraph=True)
letras = "".join(lector)
print(letras)
print(lector)
print(str(lector) )
#if lector == 'starbucks coffee':
if str(lector) == '6gbaa Coffey':
  print('verdadero')
else:
  print('falso')

if str(letras) == '6gbaa Coffey':
  print('verdadero')
else:
  print('falso')

print(len(lector))

# Draw bounding boxes
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(im, bounds)

reader = easyocr.Reader(['en','es'])

# Draw bounding boxes
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(im, bounds)

bounds

!mkdir /content/datasets
