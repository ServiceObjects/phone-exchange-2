import sys
import os

sys.path.insert(0, os.path.abspath("../phone-exchange-2-python/REST"))

from get_international_exchange_info_rest import get_international_exchange_info


def get_international_exchange_info_rest_sdk_go(is_live: bool, license_key: str) -> None:
    print("\r\n-------------------------------------------------------")
    print("PhoneExchange - GetInternationalExchangeInfo - REST SDK")
    print("-------------------------------------------------------")

    phone_number = "+18059631700"
    country = "US"

    print("\r\n* Input *\r\n")
    print(f"Phone Number : {phone_number}")
    print(f"Country      : {country}")
    print(f"License Key  : {license_key}")
    print(f"Is Live      : {is_live}")

    try:
        response = get_international_exchange_info(phone_number, country, license_key, is_live)

        print("\r\n* International Exchange Info *\r\n")
        if not hasattr(response, 'Error') or not response.Error:
            if hasattr(response, 'InternationalExchangeInfo') and response.InternationalExchangeInfo:
                if response.InternationalExchangeInfo:
                    print(f"Phone Number In     : {response.InternationalExchangeInfo.PhoneNumberIn}")
                    print(f"Country Code        : {response.InternationalExchangeInfo.CountryCode}")
                    print(f"Format National     : {response.InternationalExchangeInfo.FormatNational}")
                    print(f"Extension           : {response.InternationalExchangeInfo.Extension}")
                    print(f"Locality            : {response.InternationalExchangeInfo.Locality}")
                    print(f"Locality Match Level: {response.InternationalExchangeInfo.LocalityMatchLevel}")
                    print(f"Time Zone           : {response.InternationalExchangeInfo.TimeZone}")
                    print(f"Latitude            : {response.InternationalExchangeInfo.Latitude}")
                    print(f"Longitude           : {response.InternationalExchangeInfo.Longitude}")
                    print(f"Country             : {response.InternationalExchangeInfo.Country}")
                    print(f"Country ISO2        : {response.InternationalExchangeInfo.CountryISO2}")
                    print(f"Country ISO3        : {response.InternationalExchangeInfo.CountryISO3}")
                    print(f"Format International: {response.InternationalExchangeInfo.FormatInternational}")
                    print(f"Format E164         : {response.InternationalExchangeInfo.FormatE164}")
                    print(f"Carrier             : {response.InternationalExchangeInfo.Carrier}")
                    print(f"Line Type           : {response.InternationalExchangeInfo.LineType}")
                    print(f"SMS Address         : {response.InternationalExchangeInfo.SMSAddress}")
                    print(f"MMS Address         : {response.InternationalExchangeInfo.MMSAddress}")
                    print(f"Is Valid            : {response.InternationalExchangeInfo.IsValid}")
                    print(f"Is Valid For Region : {response.InternationalExchangeInfo.IsValidForRegion}")
                    print(f"Note Codes          : {response.InternationalExchangeInfo.NoteCodes}")
                    print(f"Note Descriptions   : {response.InternationalExchangeInfo.NoteDescriptions}")
                else:
                    print("No international exchange info items found.")
        else:
            print("No international exchange info found.")

        if response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Desc    : {response.Error.Desc}")
            print(f"Error TypeCode: {response.Error.TypeCode}")
            print(f"Error DescCode: {response.Error.DescCode}")
            print(f"Type          : {response.Error.Type}")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Error Message: {str(e)}")