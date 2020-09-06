#!/usr/bin/env python
# coding: utf-8


# Author: Vincent FOUCAULT
# ssd1306 node for Yellow robot

import time

import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import rospy
#import roslib
from yellow_oled.srv import Oled_message # read service content

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_bus=0, gpio=1) # setting gpio to 1 is hack to avoid platform detection

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
width = disp.width # read width from Adafruilt lib
height = disp.height # read height from Adafruilt lib
image = Image.new('1', (width, height)) # mode '1' for 1-bit color.

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Load default font.
text_font = '/home/yellow/catkin_ws/src/yellow_oled/uav_osd/UAV-OSD-Mono.ttf'
#font = ImageFont.load_default()
font = ImageFont.truetype(text_font, 20)

class SEND_COMMAND():

    def __init__(self):

        rospy.init_node('oled_node', anonymous=True)
	received_command = rospy.Service('oled_command', Oled_message, self.print_to_oled)

    def print_to_oled(self, command): 
      try :

	# Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

	row = command.row
	column = command.column
        command_value = command.command
        content = str(command.sentence)
        draw.text((row, column), content,  font=font, fill=255)
        # Display image.
        disp.image(image)
        disp.display()
        time.sleep(.1)
        return

      except :
      	rospy.loginfo("oled error")
	return


if __name__ == '__main__':
    try:
        send = SEND_COMMAND()
        rospy.spin()
    except rospy.ROSInterruptException:
        # Clear display.
        draw.rectangle((0,0,128,32), outline=0, fill=0)
        pass
