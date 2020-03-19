# cmake needs this line
cmake_minimum_required(VERSION 3.1)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# Define project name
PROJECT ( Multiples_of_3_and_5 )

# Set source/header directory
file(GLOB MULTIPLES_OF_3_AND_5_CPP ${CMAKE_SOURCE_DIR}/src/*.cpp)
file(GLOB MULTIPLES_OF_3_AND_5_HEADERS ${CMAKE_SOURCE_DIR}/src/*.h)

# Declare the executable target built from your sources
add_executable( Multiples_of_3_and_5 ${MULTIPLES_OF_3_AND_5_CPP} ${MULTIPLES_OF_3_AND_5_HEADERS})
