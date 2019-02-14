# cmake needs this line
cmake_minimum_required(VERSION 3.1)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# Define project name
PROJECT ( Even_Fibonacci_numbers )

# Set source/header directory
file(GLOB EVEN_FIBONACCI_NUMBERS_CPP ${CMAKE_SOURCE_DIR}/src/*.cpp)
file(GLOB EVEN_FIBONACCI_NUMBERS_HEADERS ${CMAKE_SOURCE_DIR}/src/*.h)

# Declare the executable target built from your sources
add_executable( Even_Fibonacci_numbers ${EVEN_FIBONACCI_NUMBERS_CPP} ${EVEN_FIBONACCI_NUMBERS_HEADERS})
