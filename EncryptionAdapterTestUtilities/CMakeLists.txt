cmake_minimum_required(VERSION 3.2)

# Find external dependencides
find_package(gtest)
find_package(TestUtilitiesInterface)
find_package(EncryptionAdapterInterface)

# Add project folder into includes
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Configure Encryption Adapter test utilities project
set(ENCRYPTION_ADAPTER_TEST_UTILITIES_PROJECT EncryptionAdapterTestUtilities)
file(GLOB_RECURSE ENCRYPTION_ADAPTER_TEST_UTILITIES_PROJECT_SRC "*.cpp")
file(GLOB_RECURSE ENCRYPTION_ADAPTER_TEST_UTILITIES_PROJECT_HDR "*.h")
add_library(${ENCRYPTION_ADAPTER_TEST_UTILITIES_PROJECT} STATIC ${ENCRYPTION_ADAPTER_TEST_UTILITIES_PROJECT_SRC} ${ENCRYPTION_ADAPTER_TEST_UTILITIES_PROJECT_HDR})
target_link_libraries(${ENCRYPTION_ADAPTER_TEST_UTILITIES_PROJECT} gtest::gtest TestUtilitiesInterface::TestUtilitiesInterface EncryptionAdapterInterface::EncryptionAdapterInterface)

# Configure source groups
foreach(FILE ${ENCRYPTION_ADAPTER_TEST_UTILITIES_PROJECT_SRC} ${ENCRYPTION_ADAPTER_TEST_UTILITIES_PROJECT_HDR})
    get_filename_component(PARENT_DIR "${FILE}" DIRECTORY)
    string(REPLACE "${CMAKE_CURRENT_SOURCE_DIR}" "" GROUP "${PARENT_DIR}")
    string(REPLACE "/" "\\" GROUP "${GROUP}")

    if ("${FILE}" MATCHES ".*\\.cpp")
       set(GROUP "Source Files${GROUP}")
    elseif("${FILE}" MATCHES ".*\\.h")
       set(GROUP "Header Files${GROUP}")
    endif()

    source_group("${GROUP}" FILES "${FILE}")
endforeach()
