cmake_minimum_required(VERSION 3.14)
project(PotatoDotsCounter)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)

set(CMAKE_PREFIX_PATH "/home/luna/Qt/6.7.0/gcc_64")
find_package(Qt6 REQUIRED COMPONENTS Widgets Core)
find_package(OpenCV REQUIRED)

add_executable(PotatoDotsCounter main.cpp PotatoApp.cpp ImageProcessor.cpp)
target_link_libraries(PotatoDotsCounter Qt6::Widgets Qt6::Core ${OpenCV_LIBS})
