import constants


class JsonInfoData:

    def __init__(self, info_dict):
        self.wurfl_api_version = info_dict["wurfl_api_version"]
        self.wurfl_info = info_dict["wurfl_info"]
        self.wm_version = info_dict["wm_version"]
        self.important_headers = info_dict["important_headers"]
        self.static_capabilities = info_dict["static_caps"]
        self.virtual_capabilities = info_dict["virtual_caps"]


class JsonDeviceData:

    def __init__(self, info_dict):
        self.error = info_dict["error"]
        self.api_version = info_dict["apiVersion"]
        self.capabilities = info_dict["capabilities"]
        self.mtime = int(info_dict["mtime"])
        self.ltime = info_dict["ltime"]


class Request:
    def __init__(self, lookup_headers, requestedCaps, requestedVcaps, wurflId, cache_type, important_headers):
        self.lookup_headers = lookup_headers
        self.requested_caps = requestedCaps
        self.requested_vcaps = requestedVcaps
        self.wurfl_id = wurflId
        self.cache_type = cache_type
        self.important_headers = important_headers
        self.key = None

    def __eq__(self, other):
        if self is None or other is None:
            return False
        if self.cache_type == constants.DEVICE_ID_CACHE_TYPE:
            return self.wurfl_id == other.wurfl_id
        else:
            return self.get_user_agent_cache_key() == other.get_user_agent_cache_key()

    def __hash__(self):
        return hash(self.get_user_agent_cache_key())

    def get_user_agent_cache_key(self):

        if self.key is not None:
            return self.key

        key = ""
        if (self.lookup_headers is None or len(self.lookup_headers) == 0) \
                & (constants.HEADERS_CACHE_TYPE == self.cache_type):
            self.key = ""
            return key

        # if cache type is device id we use wurfl_id as cache key
        if constants.DEVICE_ID_CACHE_TYPE == self.cache_type:
            self.key = self.wurfl_id
            return self.key

        # Using important headers array preserves header name order
        for h in self.important_headers:
            if h in self.lookup_headers:
                hval = self.lookup_headers[h]
                if hval is not None:
                    key += hval
        self.key = key
        return self.key


class WmClientError(Exception):
    def __init__(self, message):
        self.message = message
