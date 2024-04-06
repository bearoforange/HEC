import os
from PIL import Image, ImageDraw, ImageFont
import time
import textwrap

from TP_lib import epd2in13_V3

def TimeToString(struct_time: time.struct_time) -> str:
    return "{year}.{month:02d}.{day:02d} {hour:02d}:{minute:02d}:{second:02d}".format_map({
        "year": struct_time.tm_year,
        "month": struct_time.tm_mon,
        "day": struct_time.tm_mday,
        "hour": struct_time.tm_hour,
        "minute": struct_time.tm_min,
        "second": struct_time.tm_sec
    })

def TextCutter(text: str) -> str:
    wrapped = textwrap.wrap(text=text, width=15)
    if len(wrapped) > 1:
        if len(wrapped) > 2:
            return wrapped[0] + "\n" + wrapped[1] + "..."

        else:
            return wrapped[0] + "\n" + wrapped[1]

    else:
        return text

class Font():
    def __init__(self, size: int):
        fonts = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "pic"
          )

        self.font = ImageFont.truetype(
            os.path.join(fonts, "Font.ttc"), size
        )
        self.size = size


class View():
    def __init__(self):
        self.epd = epd2in13_V3.EPD()
    
    def DisplayTime(self):
        image = Image.new("1", (250, 122), 1)
        font = Font(50)
        drawer = ImageDraw.Draw(image)

        text = "{hour}:{minute:02d}".format_map({
            "hour": time.localtime().tm_hour,
            "minute": time.localtime().tm_min
        })

        drawer.text(xy=(int(((250 - drawer.textlength(text, font=font.font))) / 2), int((122 - font.size) / 2)), text=text, fill=0, font=font.font)

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.display(self.epd.getbuffer(image))
        self.epd.sleep()

    def DisplayUpcoming(self, upcoming: float):
        image = Image.new("1", (250, 122), 1)
        font = Font(24)
        drawer = ImageDraw.Draw(image)

        upcoming = int(upcoming - time.time())
        if upcoming > 86400:
            upcoming = str(upcoming//86400) + " days until"
            text = "next event"

        elif upcoming > 3600:
            upcoming = str(upcoming//3600) + " hours until"
            text = "next event"

        else:
            upcoming = str(upcoming//60) + " minutes"
            text = "until next event"

        drawer.rectangle([5, 5, 245, 117], fill=None, outline=0, width=2)
        drawer.text(xy=(int(((250 - drawer.textlength(upcoming, font=font.font))) / 2), int((120 - font.size * 2) / 2)), text=upcoming, fill=0, font=font.font)
        drawer.text(xy=(int(((250 - drawer.textlength(text, font=font.font))) / 2), int((120 - font.size * 2) / 2 + font.size + 2)), text=text, fill=0, font=font.font)

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.display(self.epd.getbuffer(image))
        self.epd.sleep()

    def DisplayLatest(self, latest: float, message: str):
        image = Image.new("1", (250, 122), 1)
        small_font = Font(18)
        big_font = Font(24)
        drawer = ImageDraw.Draw(image)

        text = TimeToString(time.localtime(latest))
        drawer.rectangle([5, 5, 245, 117], fill=None, outline=0, width=2)
        drawer.text(xy=(10, 8), text=text, fill=0, font=small_font.font)
        drawer.multiline_text(xy=(10, 30), text=TextCutter(message), fill=0, font=big_font.font, spacing=2)

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.display(self.epd.getbuffer(image))
        self.epd.sleep()

    def DisplayEvent(self, message: str):
        image = Image.new("1", (250, 122), 1)
        small_font = Font(18)
        medium_font = Font(20)
        big_font = Font(24)
        drawer = ImageDraw.Draw(image)

        text = "{hour}:{minute:02d}".format_map({
            "hour": time.localtime().tm_hour,
            "minute": time.localtime().tm_min
        })

        drawer.rectangle([5, 5, 245, 117], fill=None, outline=0, width=2)
        drawer.text(xy=(10, 8), text=text, fill=0, font=medium_font.font)
        drawer.multiline_text(xy=(10, 30), text=TextCutter(message), fill=0, font=big_font.font, spacing=2)
        drawer.text(xy=(60, 89), text="Tap to continue", fill=0, font=small_font.font)

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.display(self.epd.getbuffer(image))
        self.epd.sleep()

    def Shutdown(self):
        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.Clear(0xFF)
        self.epd.sleep()
        self.epd.Dev_exit()