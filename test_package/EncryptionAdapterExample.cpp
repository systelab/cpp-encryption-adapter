#define _SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING  1

#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include <iostream>

#include "EncryptionAdapterTestUtilities/Mocks/MockEncryptionAdapter.h"


int main(int argc, char *argv[])
{
    systelab::encryption::test_utility::MockEncryptionAdapter encryptionAdapter;
    std::cout << "Encryption adapter test utilities work as expected" << std::endl;

    return 0;
}
