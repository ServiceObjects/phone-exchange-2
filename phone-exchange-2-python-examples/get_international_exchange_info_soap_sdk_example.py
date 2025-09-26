import sys
import os

sys.path.insert(0, os.path.abspath("../phone-exchange-2-python/SOAP"))

from get_international_exchange_info_soap import GetInternationalExchangeInfoSoap

def get_international_exchange_info_soap_sdk_go(is_live: bool, license_key: str) -> None:
    print("\r\n-------------------------------------------------------")
    print("PhoneExchange - GetInternationalExchangeInfo - SOAP SDK")
    print("-------------------------------------------------------")

    phone_number = "+18059631700"
    country = "US"
    timeout_seconds = 15

    print("\r\n* Input *\r\n")
    print(f"Phone Number   : {phone_number}")
    print(f"Country        : {country}")
    print(f"License Key    : {license_key}")
    print(f"Is Live        : {is_live}")
    print(f"Timeout Seconds: {timeout_seconds}")

    try:
        service = GetInternationalExchangeInfoSoap(license_key, is_live, timeout_seconds * 1000)
        response = service.get_international_exchange_info(phone_number, country)

        if not hasattr(response, 'Error') or not response.Error:
            print("\r\n* International Exchange Info *\r\n")
            if hasattr(response, 'InternationalExchangeInfo') and response.InternationalExchangeInfo:
                print(f"Phone Number In     : {getattr(response.InternationalExchangeInfo, 'NumberIn', '')}")
                print(f"Country Code        : {getattr(response.InternationalExchangeInfo, 'CountryCode', '')}")
                print(f"Format National     : {getattr(response.InternationalExchangeInfo, 'FormatNational', '')}")
                print(f"Extension           : {getattr(response.InternationalExchangeInfo, 'Extension', '')}")
                print(f"Locality            : {getattr(response.InternationalExchangeInfo, 'Locality', '')}")
                print(f"Locality Match Level: {getattr(response.InternationalExchangeInfo, 'LocalityMatchLevel', '')}")
                print(f"Time Zone           : {getattr(response.InternationalExchangeInfo, 'TimeZone', '')}")
                print(f"Latitude            : {getattr(response.InternationalExchangeInfo, 'Latitude', '')}")
                print(f"Longitude           : {getattr(response.InternationalExchangeInfo, 'Longitude', '')}")
                print(f"Country             : {getattr(response.InternationalExchangeInfo, 'Country', '')}")
                print(f"Country ISO2        : {getattr(response.InternationalExchangeInfo, 'CountryISO2', '')}")
                print(f"Country ISO3        : {getattr(response.InternationalExchangeInfo, 'CountryISO3', '')}")
                print(f"Format International: {getattr(response.InternationalExchangeInfo, 'FormatInternational', '')}")
                print(f"Format E164         : {getattr(response.InternationalExchangeInfo, 'FormatE164', '')}")
                print(f"Carrier             : {getattr(response.InternationalExchangeInfo, 'Carrier', '')}")
                print(f"Line Type           : {getattr(response.InternationalExchangeInfo, 'LineType', '')}")
                print(f"SMS Address         : {getattr(response.InternationalExchangeInfo, 'SMSAddress', '')}")
                print(f"MMS Address         : {getattr(response.InternationalExchangeInfo, 'MMSAddress', '')}")
                print(f"Is Valid            : {getattr(response.InternationalExchangeInfo, 'IsValid', '')}")
                print(f"Is Valid For Region : {getattr(response.InternationalExchangeInfo, 'IsValidForRegion', '')}")
                print(f"Note Codes          : {getattr(response.InternationalExchangeInfo, 'NoteCodes', '')}")
                print(f"Note Descriptions   : {getattr(response.InternationalExchangeInfo, 'NoteDescriptions', '')}")
            else:
                print("No international exchange info items found.")
        else:
            print("No international exchange info found.")

        if hasattr(response, 'Error') and response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Type    : {response.Error.Type}")
            print(f"Error Desc    : {response.Error.Desc}")
            print(f"Error TypeCode: {response.Error.TypeCode}")
            print(f"Error DescCode: {response.Error.DescCode}")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Exception occurred: {str(e)}")