import os
from conans import ConanFile, tools, CMake


class EncryptionAdapterTestUtilitiesConan(ConanFile):
    name = "EncryptionAdapterTestUtilities"
    description = "Test utilities for library-agnostic API for C++ to encrypt data"
    url = "https://github.com/systelab/cpp-encryption-adapter"
    homepage = "https://github.com/systelab/cpp-encryption-adapter"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "encryption", "adapter", "wrapper", "test", "gtest")
    license = "MIT"
    generators = "cmake_find_package"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("gtest/1.14.0#4372c5aed2b4018ed9f9da3e218d18b3")
        self.requires("TestUtilitiesInterface/1.0.8@systelab/stable")
        self.requires(f"EncryptionAdapterInterface/{os.environ['VERSION']}@systelab/{os.environ['CHANNEL']}")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/EncryptionAdapterTestUtilities", keep_path=True)
        self.copy("*EncryptionAdapterTestUtilities.lib", dst="lib", keep_path=False)
        self.copy("*EncryptionAdapterTestUtilities.pdb", dst="lib", keep_path=False)
        self.copy("*EncryptionAdapterTestUtilities.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
