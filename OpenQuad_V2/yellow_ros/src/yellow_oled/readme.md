Yellow_Oled
A SSD1306 Oled screed service, working under ROS MELODIC
######################################################################
load libs :
sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install Adafruit-SSD1306

To test, execute :

write hello world ! :
rosservice call /oled_command 0, 0, 1, "hello world !"

clear screen :
rosservice call /oled_command 0, 0, 0, ""

scroll text :
rosservice call /oled_command 0, 0, 2, "hello world !"
