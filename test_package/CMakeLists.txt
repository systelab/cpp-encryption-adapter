cmake_minimum_required(VERSION 3.2)

project(EncryptionAdapterPackageTestProject)

# Configure environment
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../cmake ${CMAKE_BINARY_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Find external dependencies
find_package(EncryptionAdapterTestUtilities)

# Configure test package project
set(ENCRYPTION_ADAPTER_PACKAGE_TEST_PROJECT EncryptionAdapterPackageTest)
add_executable(${ENCRYPTION_ADAPTER_PACKAGE_TEST_PROJECT} EncryptionAdapterExample.cpp)
target_link_libraries(${ENCRYPTION_ADAPTER_PACKAGE_TEST_PROJECT} EncryptionAdapterTestUtilities::EncryptionAdapterTestUtilities)

# Register tests
enable_testing()
add_test(NAME EncryptionAdapterPackageTest COMMAND ${ENCRYPTION_ADAPTER_PACKAGE_TEST_PROJECT})
