from conans import ConanFile


class EncryptionAdapterInterfaceConan(ConanFile):
    name = "EncryptionAdapterInterface"
    description = "Interface of library-agnostic API for C++ to encrypt data"
    url = "https://github.com/systelab/cpp-encryption-adapter"
    homepage = "https://github.com/systelab/cpp-encryption-adapter"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "encryption", "adapter", "wrapper", "interface")
    license = "MIT"
    generators = "cmake_find_package"
    # No settings/options are necessary, this is header only
    exports_sources = "*.h"

    def package(self):
        self.copy("IEncryptionAdapter.h", dst="include/EncryptionAdapterInterface")

    def package_info(self):
        self.info.header_only()
