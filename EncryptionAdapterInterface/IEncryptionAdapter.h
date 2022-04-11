#pragma once

#include "SecurityKey.h"

#include <stdexcept>
#include <string>


namespace systelab { namespace encryption {

	class IEncryptionAdapter
	{
	public:
		virtual ~IEncryptionAdapter() = default;

		virtual std::string encryptString(const SecurityKey& key, const std::string& input) const = 0;
		virtual std::string decryptString(const SecurityKey& key, const std::string& input) const = 0;
		
	public:
		struct Exception : std::runtime_error
		{
			explicit Exception(const std::string& message)
				: std::runtime_error(message)
			{}
		};
	};

}}
