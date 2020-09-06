cmake_minimum_required(VERSION 3.0.2)
project(yellow_neopixels)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_srvs
  message_generation
)

 add_service_files(
   DIRECTORY srv
   FILES neopixels_message.srv
)

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_srvs
#   std_msgs  # Or other packages containing msgs
) 	


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES qbo_talk
  CATKIN_DEPENDS rospy std_srvs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  ${catkin_INCLUDE_DIRS}
)
