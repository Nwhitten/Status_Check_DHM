#!/usr/bin/env python3
import sys
import os
import json
import urllib.request, urllib.error, urllib.parse#!/usr/bin/env python3
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7789
from datetime import datetime

# Create ST7789 LCD display class.

disp = ST7789.ST7789(
    height=240,
    width=320,
    rotation=180,
    port=0,
    cs=1,
    dc=9,
    backlight=13,
    spi_speed_hz=60 * 1000 * 1000,
    offset_left=0,
    offset_top=0)


# Initialize display.
disp.begin()

width = disp.width
height = disp.height

#font_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",28)
#fontsm_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",19)
#fontti_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",16)
#fontex_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",11)

font_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",30)
#fontsm_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",25)
fontti_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",25)
fontex_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",20)


while True:


        try:
                f = urllib.request.urlopen('http://pihole.local/admin/api.php')
                json_string = f.read()
                parsed_json = json.loads(json_string)
                adsblocked = parsed_json['ads_blocked_today']
                ratioblocked = parsed_json['ads_percentage_today']
                holestatus = parsed_json['status']
  
                dns_queries_today = parsed_json['dns_queries_today']
                unique_clients  = parsed_json['unique_clients']
                dns_queries  = parsed_json['dns_queries_all_types']
                blocked_domains  = parsed_json['domains_being_blocked']
  
                f.close()
        except:
                queries = '?'
                adsblocked = '?'
                ratio = '?'

        if  str(holestatus) == 'enabled':
                img = Image.open("/usr/local/bin/status_check_DHM/DHM_pihole.jpg")
                draw = ImageDraw.Draw(img)
                status_output = 'Enabled'
                status_output_w, status_output_h = font_ArialB.getsize(status_output)
                status_output_x = int((width - status_output_w) / 2)
                draw.text((status_output_x,0), status_output, (0,0,0), font_ArialB)
        
        
        else:
                img = Image.new("RGB",(width,height),(255,255,255))
                draw = ImageDraw.Draw(img)
                status_output = 'Disabled'
                status_output_w, status_output_h = font_ArialB.getsize(status_output)
                status_output_x = int((width - status_output_w) / 2)
                draw.rectangle((0, 0, width, status_output_h+4), (255, 0, 0))

                #draw.text((status_output_x,0), status_output, (254,254,254), font_ArialB)

                draw.text((100,100), str(status_output_h), (0,0,0), font_ArialB)





        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        

        #status_output = 'Enabled'
        status_output_w, status_output_h = font_ArialB.getsize(status_output)
        status_output_x = int((width - status_output_w) / 2)

        draw.text((0,40), 'Total queries (' + str(unique_clients) + ' clients)      ' , (0,0,0), fontex_ArialB)
        draw.text((5,60), str(dns_queries) , (0,0,0), fontti_ArialB)

        draw.text((0,90), 'Queries Blocked' , (0,0,0), fontex_ArialB)
        draw.text((5,110), str(adsblocked) , (0,0,0), fontti_ArialB)

        draw.text((0,140), 'Percent Blocked' , (0,0,0), fontex_ArialB)
        draw.text((5,160), str("%.1f" % round(ratioblocked,2)) + "% ", (0,0,0), fontti_ArialB)

        draw.text((0,190), 'Domains on Blocklist' , (0,0,0), fontex_ArialB)
        draw.text((5,210), str(blocked_domains), (0,0,0), fontti_ArialB)

        draw.text((210,210),str(current_time), (255,0,0), fontti_ArialB)
        disp.display(img)
        time.sleep(300)
        
        
        
#.reset()
#import ST7789  
# from PIL import Image  
# from time import sleep  
# display=ST7789.ST7789(port=0,cs=0,rst=6,dc=5,backlight=4,spi_speed_hz=160000000)  
# display._spi.mode=3  
# display.reset()  
# display._init()  
# image=Image.new('RGB',(240,240),(255,0,0))  #('RGB',(240,240),(r,g,b))
# display.display(image)  
# sleep(2)  
# image=Image.open("image5.jpg")  
# image=image.resize((240,240),resample=Image.LANCZOS)  
# display.display(image) 

#carrier.display.enableDisplay(false);

    #carrier.display.fillScreen(ST77XX_BLACK);
    #pinMode(TFT_BACKLIGHT, OUTPUT);
    #digitalWrite(TFT_BACKLIGHT, LOW);
    #delay(5000);
    #digitalWrite(TFT_BACKLIGHT, HIGH);