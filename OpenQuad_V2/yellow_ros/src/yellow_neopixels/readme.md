Yellow_neopixels
Robot front sticks leds service, working under ROS MELODIC
######################################################################
load libs :
pip install adafruit-circuitpython-neopixel

To test, execute :

write hello world ! :
rosservice call /oled_command 0, 0, 1, "hello world !"

