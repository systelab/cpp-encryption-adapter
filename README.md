[![Build Status](https://travis-ci.org/systelab/cpp-encryption-adapter.svg?branch=master)](https://travis-ci.org/systelab/cpp-encryption-adapter)
[![Build status](https://ci.appveyor.com/api/projects/status/ruikmrb5myae2ovn?svg=true)](https://ci.appveyor.com/project/systelab/cpp-encryption-adapter)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7e19c714d00244419ea2bdc5401e7cc6)](https://www.codacy.com/app/systelab/cpp-encryption-adapter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=systelab/cpp-encryption-adapter&amp;utm_campaign=Badge_Grade)
[![JSONAdapterInterface](https://api.bintray.com/packages/systelab/conan/EncryptionAdapterInterface:systelab/images/download.svg)](https://bintray.com/systelab/conan/EncryptionAdapterInterface:systelab/_latestVersion)


# C++ Encryption Adapter interface

This repository defines a library-agnostic API for C++ to encrypt data symmetrically.

## Supported features

* String encryption / decryption

## Available implementations

* None public

## Usage

Use of adapter features begins with an instance of `systelab::encryption::IEncryptionAdapter` class. See documentation of selected implementation for details about how to build one.

### String encryption / decryption

Encrypt a given input string using a password/secret:

```cpp
std::unique_ptr<systelab::encryption::IEncryptionAdapter> encryptionAdapter = ...;
std::string input = "This is the string to be encrypted";
std::string password = "P@ssw0rdG0esHere";
std::string encryptedData = encryptionAdapter->encryptString(input, password);
```

The obtained string can be decrypted as follows:

```cpp
std::string decryptedData = encryptionAdapter->decryptString(encryptedData, password);
```

At this point, the returned `decryptedData` string should have the same value than the initial `input` string.
