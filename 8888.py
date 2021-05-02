from PIL import Image,ImageFilter
import telebot
import sys
from telebot import types
token =('1738813755:AAGbXklgKrAkB5PcfdGf67cMUao3A9RujYI')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def startKBoard(message):
    message_text = 'Hi! I will help you make your picture completely new!'
    bot.send_message(message.chat.id, message_text)
    startKBoard = telebot.types.ReplyKeyboardMarkup(True)
    startKBoard.row('size', 'filter','blur')
    startKBoard.row('reverse','sharpen','jpg to png')
    bot.send_message(message.chat.id, "First, send me your photo. Secondly, choose what you want to do with it", reply_markup=startKBoard)

@bot.message_handler(content_types=['photo'])
def photo(message):
    print ('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print ('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print ('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
image=Image.open("image.jpg")

def ssharpen(message):
    ss=image.filter(ImageFilter.SHARPEN)
    ss.save("sharpen" + ".jpg")
    bot.send_message(message.chat.id, "Filter sharpen:")
    bot.send_photo(message.chat.id, photo=open('sharpen.jpg', "rb"))

def png(message):
    try:
        pp = Image.open("image.jpg")
    except IOError:
        print("Unable to load image")
        sys.exit(1)
    pp.save('topng.png', 'png')
    bot.send_message(message.chat.id, "JPG to PNG:")
    bot.send_photo(message.chat.id, photo=open('topng.png', "rb"))

def bblur(message):
    blurKBoard = telebot.types.ReplyKeyboardMarkup(True)
    blurKBoard.row('slight blur','medium blur','strong blur')
    blurKBoard.row('back')
    bot.send_message(message.chat.id, "Select the level of blur:", reply_markup=blurKBoard)
def slight(message):
    b1=image.filter(ImageFilter.GaussianBlur(radius=1))
    b1.save("blur1" + ".jpg")
    bot.send_message(message.chat.id, "Filter Blur(slight):")
    bot.send_photo(message.chat.id, photo=open('blur1.jpg', "rb"))
def medium(message):
    b2=image.filter(ImageFilter.GaussianBlur(radius=3))
    b2.save("blur2" + ".jpg")
    bot.send_message(message.chat.id, "Filter Blur(medium):")
    bot.send_photo(message.chat.id, photo=open('blur2.jpg', "rb"))
def strong(message):
    b3=image.filter(ImageFilter.GaussianBlur(radius=5))
    b3.save("blur3" + ".jpg")
    bot.send_message(message.chat.id, "Filter Blur(strong):")
    bot.send_photo(message.chat.id, photo=open('blur3.jpg', "rb"))
def rrotate (message):
    s=(128,128)
    m=image.thumbnail(s)
    m.save(("mini" + ".jpg"))
    bot.send_message(message.chat.id, "Mini Version:")
    bot.send_photo(message.chat.id, photo=open('mini.jpg', "rb"))
def rreverse(message):
    rKBoard = telebot.types.ReplyKeyboardMarkup(True)
    rKBoard.row('45 d.','90 d.','180 d.')
    rKBoard.row('270 d.','back','360 d.')
    bot.send_message(message.chat.id, "Choose degree", reply_markup=rKBoard)

def r1(message):
    r1=image.rotate(90)
    r1.save(("90" + ".jpg"))
    bot.send_message(message.chat.id, "Rotate 90 degrees::")
    bot.send_photo(message.chat.id, photo=open('90.jpg', "rb"))

def r2(message):
    r2=image.rotate(45)
    r2.save(("45" + ".jpg"))
    bot.send_message(message.chat.id, "Rotate 45 degrees::")
    bot.send_photo(message.chat.id, photo=open('45.jpg', "rb"))

def r3(message):
    r3=image.rotate(180)
    r3.save(("180" + ".jpg"))
    bot.send_message(message.chat.id, "Rotate 180degrees::")
    bot.send_photo(message.chat.id, photo=open('180.jpg', "rb"))
def r4(message):
    r4=image.rotate(270)
    r4.save(("270" + ".jpg"))
    bot.send_message(message.chat.id, "Rotate 270 degrees::")
    bot.send_photo(message.chat.id, photo=open('270.jpg', "rb"))

def r5(message):
    r5=image.rotate(360)
    r5.save(("360" + ".jpg"))
    bot.send_message(message.chat.id, "Rotate 360 degrees::")
    bot.send_photo(message.chat.id, photo=open('360.jpg', "rb"))
def ssize(message):
    a=image.format
    a2=(image).size
    a3=image.mode
    print(a2)
    bot.send_message(message.chat.id, "Image size:")
    bot.send_message(message.chat.id,a)
    bot.send_message(message.chat.id,a2)
    bot.send_message(message.chat.id,a3)

def ffilter(message):
    if message.text == "filter":
        filterKBoard = telebot.types.ReplyKeyboardMarkup(True)
        filterKBoard.row('f1','f2','f3')
        filterKBoard.row('f4','f5','f6')
        filterKBoard.row('f7','f8','f9')
        filterKBoard.row('f10','back','f11')
        bot.send_message(message.chat.id, "Choose filter:", reply_markup=filterKBoard)


def ff1(message):
    b=image.filter(ImageFilter.CONTOUR)
    b.save("CONTOUR" + ".jpg")
    bot.send_message(message.chat.id, "Filter CONTOUR:")
    bot.send_photo(message.chat.id, photo=open('CONTOUR.jpg', "rb"))

def ff2(message):
    img= image.filter(ImageFilter.DETAIL)
    img.save("DETAIL" + ".jpg")
    bot.send_message(message.chat.id, "Filter Detail :")
    bot.send_photo(message.chat.id, photo=open('DETAIL.jpg', 'rb'))

def ff3(message):
    img= image.filter(ImageFilter.EDGE_ENHANCE)
    img.save("EDGE_ENHANCE" + ".jpg")
    bot.send_message(message.chat.id, "Filter Edge enhance:")
    bot.send_photo(message.chat.id, photo=open('EDGE_ENHANCE.jpg', 'rb'))

def ff4(message):
    img= image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    img.save("EDGE_ENHANCE_MORE" + ".jpg")
    bot.send_message(message.chat.id, "Filter edge enhance more:")
    bot.send_photo(message.chat.id, photo=open('EDGE_ENHANCE_MORE.jpg', 'rb'))

def ff5(message):
    img= image.filter(ImageFilter.EMBOSS)
    img.save("EMBOSS" + ".jpg")
    bot.send_message(message.chat.id, "Filter Emboss:")

    bot.send_photo(message.chat.id, photo=open('EMBOSS.jpg', 'rb'))

def ff6(message):
    img= image.filter(ImageFilter.FIND_EDGES)
    img.save("FIND_EDGES" + ".jpg")
    bot.send_message(message.chat.id, "Filter Find Edges:")
    bot.send_photo(message.chat.id, photo=open('FIND_EDGES.jpg', 'rb'))

def ff7(message):
    img= image.filter(ImageFilter.SMOOTH)
    img.save("SMOOTH" + ".jpg")
    bot.send_message(message.chat.id, "Filter Smooth:")
    bot.send_photo(message.chat.id, photo=open('SMOOTH.jpg', 'rb'))

def ff8(message):
    img= image.filter(ImageFilter.SHARPEN)
    img.save("SHARPEN" + ".jpg")
    bot.send_message(message.chat.id, "Filter Sharpen:")
    bot.send_photo(message.chat.id, photo=open('SHARPEN.jpg', 'rb'))

def ff9(message):
    img= image.filter(ImageFilter.SMOOTH_MORE)
    img.save("SMOOTH_MORE" + ".jpg")
    bot.send_message(message.chat.id, "Filter Smooth more:")
    bot.send_photo(message.chat.id, photo=open('SMOOTH_MORE.jpg', 'rb'))
def ff10(message):
    img= image.convert('L')
    img.save("BW" + ".jpg")
    bot.send_message(message.chat.id, "Filter black-white:")
    bot.send_photo(message.chat.id, photo=open('BW.jpg', 'rb'))
def ff11(message):
    def tonegative(image):
        return 255 -image
    image.save("Negative" + ".jpg")
    bot.send_message(message.chat.id, "Filter Negative:")
    bot.send_photo(message.chat.id, photo=open('Negative.jpg', 'rb'))
def bback(message):
    backKBoard = telebot.types.ReplyKeyboardMarkup(True)
    backKBoard.row('size', 'filter','blur')
    backKBoard.row('reverse','sharpen','jpg to png')
    bot.send_message(message.chat.id, "Choose what you want to do with it:", reply_markup=backKBoard)
@bot.message_handler(content_types=['text'])
def send_text(message):
    us = message.text.lower()
    if us == 'size':
        ssize(message)
    elif us == 'filter':
        ffilter(message)
    elif us == 'sharpen':
        ssharpen(message)
    elif us== 'jpg to png':
        png(message)
    elif us == 'blur':
        bblur(message)
    elif us == 'slight blur':
        slight(message)
    elif us == 'medium blur':
        medium(message)
    elif us == 'strong blur':
        strong(message)
    elif us == 'reverse':
        rreverse(message)
    elif us == '45 d.':
        r2(message)
    elif us == '90 d.':
        r1(message)
    elif us == '180 d.':
        r3(message)
    elif us == '270 d.':
        r4(message)
    elif us == '360 d.':
        r5(message)
    elif us == 'f1':
        ff1(message)
    elif us == 'f2':
        ff2(message)
    elif us == 'f3':
        ff3(message)
    elif us == 'f4':
        ff4(message)
    elif us == 'f5':
        ff5(message)
    elif us == 'f6':
        ff6(message)
    elif us == 'f7':
        ff7(message)
    elif us == 'f8':
        ff8(message)
    elif us == 'f9':
        ff9(message)
    elif us == 'f10':
        ff10(message)
    elif us == 'f11':
        ff11(message)
    elif us == 'back':
        bback(message)
bot.polling()