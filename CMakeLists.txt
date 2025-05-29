cmake_minimum_required(VERSION 3.15...3.18)
project(fwdpy11_exponential_fitness)

# As of 0.8.0, fwdpy11
# is compiled with the C++14 language
# standard (-std=c++14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD 14) 
find_package(Python COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG)
message(STATUS "Found pybind11: ${pybind11_VERSION}")
if(${pybind11_VERSION} VERSION_LESS '2.12.0')
    message(FATAL_ERROR "pybind11 version must be >= '2.12.0'")
endif()

execute_process(COMMAND python3 -m fwdpy11 --fwdpy11_headers OUTPUT_VARIABLE FP11HEADERS)
execute_process(COMMAND python3 -m fwdpy11 --fwdpp_headers OUTPUT_VARIABLE FWDPPHEADERS)

# find_package(GSL REQUIRED)
include_directories(BEFORE ${FP11HEADERS} ${FWDPPHEADERS})
# message(STATUS "GSL headers in ${GSL_INCLUDE_DIRS}")
# include_directories(BEFORE ${GSL_INCLUDE_DIRS})


set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -Wall -Wextra -Weffc++ -Woverloaded-virtual -Wold-style-cast -Werror=effc++ -Werror=old-style-cast -Werror=overloaded-virtual -Werror=unused-parameter")

pybind11_add_module(_exponential_fitness MODULE src/exponential_fitness.cc)
set_target_properties(_exponential_fitness PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_link_directories(_exponential_fitness PRIVATE ${CMAKE_SOURCE_DIR}/fwdpy11_exponential_fitness)
install(TARGETS _exponential_fitness DESTINATION fwdpy11_exponential_fitness)
