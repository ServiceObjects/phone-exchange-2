from get_exchange_info_rest_sdk_example import get_exchange_info_rest_sdk_go
from get_exchange_info_soap_sdk_example import get_exchange_info_soap_sdk_go
from get_international_exchange_info_rest_sdk_example import get_international_exchange_info_rest_sdk_go
from get_international_exchange_info_soap_sdk_example import get_international_exchange_info_soap_sdk_go

if __name__ == "__main__":
    # Your license key from Service Objects.  
    # Trial license keys will only work on the trial environments and production  
    # license keys will only work on production environments.
    #   
    license_key = "LICENSE KEY"  
    is_live = True

    # PhoneExchange2 - GetExchangeInfo - REST SDK
    get_exchange_info_rest_sdk_go(is_live, license_key)

    # PhoneExchange2 - GetExchangeInfo - SOAP SDK
    get_exchange_info_soap_sdk_go(is_live, license_key)

    # PhoneExchange2 - GetInternationalExchangeInfo - REST SDK
    get_international_exchange_info_rest_sdk_go(is_live, license_key)

    # PhoneExchange2 - GetInternationalExchangeInfo - SOAP SDK
    get_international_exchange_info_soap_sdk_go(is_live, license_key)


