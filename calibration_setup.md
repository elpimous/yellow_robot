# OpenQuad calibration setup
To use with Maurice RAHME package : https://github.com/moribots/spot_mini_mini
#

Servos connection check :
------------------------------
Be sure to check servos order, or some damages could appear on servos or plastic robot strucure !

 See Mano diagram, in doc : /OpenQuad_V2/images/SPOT MICRO Controller Manual.docx


- M01 front left shoulder, ( pin 1 on board, where teensy is plugged ! )
- M02 front left elbow,
- M03 front left wrist,
- M04 front right shoulder,
- M05 front right elbow,
- M06 front right wrist,
- M07 back left shoulder,
- M08 back left elbow,
- M09 back left wrist,
- M10 back right shoulder,
- M11 back right elbow,
- M12 back right wrist.

 
Enter servos specs on teensy board firmware :
------------------

- Open main.cpp file, (./spot_mini_mini/spot_real/Control/Teensy/SpotMiniMini/src/main.cpp)

- Modify servo range and it max/min pwm, regarding to your servos specs,
Here, you can see my servos specs (180°, and 500/2500 pwm limits).
![Alt text](/OpenQuad_V2/images/main_servo_specs.png?raw=true "Openquad")


- Next, modify teensy boot mode to "**NOMINAL_PWM**": 
![Alt text](/OpenQuad_V2/images/main_nominal.png?raw=true "Openquad")


Flash teensy :
------------------

- check and re-check that teensy isn't already powered (with Maurice, Adham, or Mano boards)
- connect micro_usb to Teensy, other part to PC,
- install plateformio : 

**sudo pip install PlatformIO**
- install needed libs : 

**pio lib install "adafruit/Adafruit Unified Sensor"**
	
**pio lib install "adafruit/Adafruit BNO055"**
	
- go to teensy firmware package : /spot_mini_mini/spot_real/Control/Teensy/SpotMiniMini/
- run terminal command : **platformio run -t upload**

after a while....teensy will be **flashed** (it led will change from **orange to red**, and will **return to orange**)

	Now, your teensy boots on NOMINAL_PWM mode !!!

------------------
------------------

Mount your servos, and lock them like on picture, as best as possible :
------------------

![Alt text](/OpenQuad_V2/images/straight_pose.png?raw=true "Openquad")


------------------



Now, we need to **find PWM correct values**, to "calibrate" servos (all same servos are not always equal) :

**install Ros_package :**

- install ros_melodic,
- navigate to catkin_ws/src/
- create a Directory (ex: yellow_dog)
- in this directory, copy the following dirs : mini_ros, spot_bullet, spot_micro, and spot_real
- navigate to ~/catkin_ws
- run terminal command : **catkin_make**

Let's go for calibration. (assume that your teensy is correctly connected to your master_board (jetson nano, RPI...), serial and 5v conected)

	Robot legs should be straight, and 90° to body (like on previous picture)

- run terminal command : **roslaunch mini_ros spot_calibrate.launch**

- open a new terminal and enter the following command : **rosservice call /servo_calibraton   and press 2 times on TAB**.

You'll see complete command needed to interact with all specific servos angles.


	Start gently, with pwm order, to avoid a burnt servo (with over range_limit order)

- Find values, corresponding to logic positions ( 0°, 90°, 180°) (ex: shoulder completely rear, perpendicular_to_body, front...)

Take time to do your best in PWM precision !!!

- Next, enter YOUR OWN values in main.cpp, in initialize() section, see picture :

![Alt text](/OpenQuad_V2/images/main_initialize.png?raw=true "Openquad")


Remember : those values are mine, for my 180°servos. Keep this in mind, and modify to your setup !

- When all values entered, change MODE to **STRAIGHT_LEGS**:

![Alt text](/OpenQuad_V2/images/main_straight.png?raw=true "Openquad")

- Flash Teensy (BE SURE TO **REMOVE** IT **5V POWER  BEFORE CONNECTING WITH USB**)

You should confirm the following robot_pose :

![Alt text](/OpenQuad_V2/images/straight_pose.png?raw=true "Openquad")

If OK, test the next MODE, either, return to servos calibration !


- Next mode, change in main.cpp the MODE to **PERPENDICULAR_LEGS**:

![Alt text](/OpenQuad_V2/images/main_perpendicular.png?raw=true "Openquad")

- Flash

You should confirm the following robot_pose :

![Alt text](/OpenQuad_V2/images/perpendicular_pose.png?raw=true "Openquad")



- Next mode, change in main.cpp the **MODE to LIEDOWN**:
![Alt text](/OpenQuad_V2/images/main_liedown.png?raw=true "Openquad")

- Flash

You should confirm the following robot_pose :
![Alt text](/OpenQuad_V2/images/liedown_pose.png?raw=true "Openquad")



- To finish, go to **RUN** MODE :

![Alt text](/OpenQuad_V2/images/main_run.png?raw=true "Openquad")

- Flash

Robot should adopt the following pose :

![Alt text](/OpenQuad_V2/images/run_pose.png?raw=true "Openquad")

------------------
------------------

# CALIBRATION DONE !!!

------------------
------------------


For infos : Teensy 4.1 diagram :

	
------------------


![Alt text](/OpenQuad_V2/images/teensy41.png?raw=true "Openquad")

