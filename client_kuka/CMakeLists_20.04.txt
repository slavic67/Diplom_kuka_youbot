cmake_minimum_required(VERSION 3.0.2)
project(kuka)

## enable C++ 11
SET(CMAKE_CXX_STANDARD 11)
## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## check required prerequisites
SET(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/external/cmake_modules")
SET(Boost_USE_STATIC_LIBS ON)
SET(Boost_ADDITIONAL_VERSIONS "1.39" "1.39.0" "1.40" "1.40.0" "1.41" "1.41.0" "1.42" "1.42.0" "1.43" "1.43.0" "1.44" "1.44.0" "1.45" "1.45.0" "1.46" "1.46.0")
FIND_PACKAGE(Boost REQUIRED COMPONENTS thread date_time filesystem system)
FIND_LIBRARY(YouBotDriver REQUIRED)
FIND_LIBRARY(soem REQUIRED)


## preprocessor definitions
SET(CMAKE_C_FLAGS_DEBUG "-fPIC -Wall -g")
SET(CMAKE_CXX_FLAGS_DEBUG "-fPIC -Wall -g")

## build parameters and paths
SET(CMAKE_BUILD_TYPE Debug) #enable debug mode (e.g. for embedded gdb in eclipse )
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin CACHE PATH "Configure the executable output path.")


## Set include directories
INCLUDE_DIRECTORIES(
	${Boost_INCLUDE_DIR}
)
## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)



## Generate services in the 'srv' folder
add_service_files(
  FILES
  AngleValues.srv
  
)



## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES kuka
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


catkin_install_python(PROGRAMS
  scripts/KUKA_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


add_executable(KUKA_client src/KUKA_client.cpp)
target_link_libraries(KUKA_client 
  ${catkin_LIBRARIES}
  YouBotDriver
	${Boost_LIBRARIES}
	pthread
	soem)
add_dependencies(KUKA_client kuka_gencpp)

OPTION(USE_SETCAP "Set permissions to access ethernet interface without sudo" ON)

#  add_custom_command(TARGET add_two_ints_client POST_BUILD
#      COMMAND ${SUDO_COMMAND} setcap cap_net_raw+ep $<TARGET_FILE:add_two_ints_client>
#  )    