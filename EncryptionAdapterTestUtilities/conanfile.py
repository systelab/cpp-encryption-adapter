import os
from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import collect_libs, copy


class EncryptionAdapterTestUtilitiesConan(ConanFile):
    required_conan_version = ">=2.0.0"
    name = "encryption-adapter-test-utilities"
    description = "Test utilities for library-agnostic API for C++ to encrypt data"
    url = "https://github.com/systelab/cpp-encryption-adapter"
    homepage = "https://github.com/systelab/cpp-encryption-adapter"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "encryption", "adapter", "wrapper", "test", "gtest")
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "*.h", "*.cpp", "**/*.h", "**/*.cpp", "!build*/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        CMakeDeps(self).generate()
        CMakeToolchain(self).generate()

    def requirements(self):
        self.requires("gtest/1.14.0")
        self.requires("test-utilities-interface/1.1.0")
        if not self.version:
            raise ConanInvalidConfiguration(
                "Pass --version when installing this recipe to resolve "
                "encryption-adapter-interface"
            )
        self.requires(f"encryption-adapter-interface/{self.version}", transitive_headers=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        include_dir = os.path.join(
            self.package_folder, "include", "EncryptionAdapterTestUtilities"
        )
        lib_dir = os.path.join(self.package_folder, "lib")
        copy(
            self, "**/*.h", src=self.source_folder, dst=include_dir,
            keep_path=True,
        )
        for extension in ("lib", "pdb", "a"):
            copy(
                self, f"**/*EncryptionAdapterTestUtilities.{extension}",
                src=self.build_folder, dst=lib_dir, keep_path=False,
            )

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
        self.cpp_info.set_property(
            "cmake_file_name", "EncryptionAdapterTestUtilities"
        )
        self.cpp_info.set_property(
            "cmake_target_name",
            "EncryptionAdapterTestUtilities::EncryptionAdapterTestUtilities",
        )
