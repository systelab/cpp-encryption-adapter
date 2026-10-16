import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy


class EncryptionAdapterTestUtilitiesTestConan(ConanFile):
    required_conan_version = ">=2.0.0"
    settings = "os", "compiler", "build_type", "arch"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        CMakeDeps(self).generate()
        CMakeToolchain(self).generate()
        runtime_bin = os.path.join(self.build_folder, "bin")
        for dep in self.dependencies.values():
            for bindir in dep.cpp_info.bindirs:
                if os.path.isdir(bindir):
                    copy(self, "*.dll", src=bindir, dst=runtime_bin)
            for libdir in dep.cpp_info.libdirs:
                if os.path.isdir(libdir):
                    copy(self, "*.dylib*", src=libdir, dst=runtime_bin)
                    copy(self, "*.so*", src=libdir, dst=runtime_bin)

    def requirements(self):
        self.requires(self.tested_reference_str)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        cmake = CMake(self)
        cmake.test()
