[![Build Status](https://travis-ci.org/systelab/cpp-encryption-adapter.svg?branch=master)](https://travis-ci.org/systelab/cpp-encryption-adapter)
[![Build status](https://ci.appveyor.com/api/projects/status/ruikmrb5myae2ovn?svg=true)](https://ci.appveyor.com/project/systelab/cpp-encryption-adapter)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d7812dbf0bf64e45bf4078aee7ad6259)](https://www.codacy.com/gh/systelab/cpp-encryption-adapter/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=systelab/cpp-encryption-adapter&amp;utm_campaign=Badge_Grade)


# C++ Encryption Adapter interface

This repository defines a library-agnostic API for C++ to encrypt data.

## Supported features

* String encryption / decryption

## Available implementations

* [Caeser Cypher](https://github.com/systelab/cpp-caeser-cypher-encryption-adapter) (only for demo purposes)
* See private repositories for production-ready implementations

## Usage

Use of adapter features begins with an instance of `systelab::encryption::IEncryptionAdapter` class. See documentation of selected implementation for details about how to build one.

### String encryption / decryption

Encrypt a given input string using a password/secret:

```cpp
std::unique_ptr<systelab::encryption::IEncryptionAdapter> encryptionAdapter = ...;
systelab::encryption::SecurityKey password = [](){ return std::string("P@ssw0rdG0esHere"); };
std::string input = "This is the string to be encrypted";
std::string encryptedData = encryptionAdapter->encryptString(password, input);
```

The obtained string can be decrypted as follows:

```cpp
std::string decryptedData = encryptionAdapter->decryptString(password, encryptedData);
```

At this point, the returned `decryptedData` string should have the same value than the initial `input` string.
