import os

from conan import ConanFile
from conan.tools.files import copy


class EncryptionAdapterInterfaceConan(ConanFile):
    required_conan_version = ">=2.0.0"
    name = "encryption-adapter-interface"
    description = "Interface of library-agnostic API for C++ to encrypt data"
    url = "https://github.com/systelab/cpp-encryption-adapter"
    homepage = "https://github.com/systelab/cpp-encryption-adapter"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "encryption", "adapter", "wrapper", "interface")
    license = "MIT"
    package_type = "header-library"
    # No settings/options are necessary, this is header only
    exports_sources = "*.h"

    def package(self):
        dst = os.path.join(
            self.package_folder, "include", "EncryptionAdapterInterface"
        )
        copy(self, "IEncryptionAdapter.h", src=self.source_folder, dst=dst)
        copy(self, "SecurityKey.h", src=self.source_folder, dst=dst)

    def package_info(self):
        self.cpp_info.set_property(
            "cmake_file_name", "EncryptionAdapterInterface"
        )
        self.cpp_info.set_property(
            "cmake_target_name",
            "EncryptionAdapterInterface::EncryptionAdapterInterface",
        )
