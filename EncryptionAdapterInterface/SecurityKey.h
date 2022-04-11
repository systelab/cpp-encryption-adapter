#pragma once

#include <functional>
#include <string>

namespace systelab { namespace encryption {
	typedef std::function<std::string()> SecurityKey;
}};
