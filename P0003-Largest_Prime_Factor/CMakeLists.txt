# cmake needs this line
cmake_minimum_required(VERSION 3.1)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# Define project name
PROJECT ( Largest_prime_factor )

# Set source/header directory
file(GLOB LARGEST_PRIME_FACTOR_CPP ${CMAKE_SOURCE_DIR}/src/*.cpp)
file(GLOB LARGEST_PRIME_FACTOR_HEADERS ${CMAKE_SOURCE_DIR}/src/*.h)

# Declare the executable target built from your sources
add_executable( Largest_prime_factor ${LARGEST_PRIME_FACTOR_CPP} ${LARGEST_PRIME_FACTOR_HEADERS})
