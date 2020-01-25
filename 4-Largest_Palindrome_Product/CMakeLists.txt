# cmake needs this line
cmake_minimum_required(VERSION 3.1)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# Define project name
PROJECT ( Largest_palindrome_product )

# Set source/header directory
file(GLOB LARGEST_PALINDROME_PRODUCT_CPP ${CMAKE_SOURCE_DIR}/src/*.cpp)
file(GLOB LARGEST_PALINDROME_PRODUCT_HEADERS ${CMAKE_SOURCE_DIR}/src/*.h)

# Declare the executable target built from your sources
add_executable( Largest_palindrome_product ${LARGEST_PALINDROME_PRODUCT_CPP} ${LARGEST_PALINDROME_PRODUCT_HEADERS})
