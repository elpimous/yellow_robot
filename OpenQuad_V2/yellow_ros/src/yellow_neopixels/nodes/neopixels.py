#!/usr/bin/env python
# coding: utf-8


# Author: Vincent FOUCAULT
# Neopixels 8x sticks node for Yellow robot head

# https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel

import time

import board
import neopixel as NPix

import rospy
#import roslib
from yellow_neopixels.srv import neopixels_message # read service content


class SEND_COMMAND():

    def __init__(self):

        rospy.init_node('neopixels8x_node', anonymous=True)

        self.leds = NPix.NeoPixel(board.NEOPIXEL, 2, auto_write=False)

	received_command = rospy.Service('neopixels_command', neopixels_message, self.read_orders)

    def read_orders(self, command): 
      try :
        # recover orders from service...
	left_stick_data = command.data1
        right_stick_data = command.data2
        self.send_to_leds_stick(left_stick_data, right_stick_data)
        return

      except :
      	rospy.loginfo("neopixels error")
	return


    def send_to_leds_stick(self, left_data, right_data):
        # feed datas
        self.leds[0] = left_data
        self.leds[1] = right_data
        # send to hardware
        self.leds.show()
        


if __name__ == '__main__':
    try:
        send = SEND_COMMAND()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
