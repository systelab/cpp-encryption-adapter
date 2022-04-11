#pragma once

#include "EncryptionAdapterInterface/IEncryptionAdapter.h"


namespace systelab { namespace encryption { namespace test_utility {

	class MockEncryptionAdapter : public IEncryptionAdapter
	{
	public:
		MockEncryptionAdapter();
		virtual ~MockEncryptionAdapter();

		MOCK_CONST_METHOD2(encryptString, std::string(const SecurityKey& key, const std::string& input));
		MOCK_CONST_METHOD2(decryptString, std::string(const SecurityKey& key, const std::string& input));
	};

}}}
