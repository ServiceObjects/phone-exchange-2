import sys
import os

sys.path.insert(0, os.path.abspath("../phone-exchange-2-python/SOAP"))

from get_exchange_info_soap import GetExchangeInfoSoap


def get_exchange_info_soap_sdk_go(is_live: bool, license_key: str) -> None:
    print("\r\n------------------------------------------")
    print("PhoneExchange - GetExchangeInfo - SOAP SDK")
    print("------------------------------------------")

    phone_number = "805-555-1212"
    timeout_seconds = 15

    print("\r\n* Input *\r\n")
    print(f"Phone Number   : {phone_number}")
    print(f"License Key    : {license_key}")
    print(f"Is Live        : {is_live}")
    print(f"Timeout Seconds: {timeout_seconds}")

    try:
        service = GetExchangeInfoSoap(license_key, is_live, timeout_seconds * 1000)
        response = service.get_exchange_info(phone_number)

        if not hasattr(response, 'Error') or not response.Error:
            print("\r\n* Exchange Info *\r\n")
            if hasattr(response, 'ExchangeInfoResults') and response.ExchangeInfoResults:
                items = response.ExchangeInfoResults.ExchangeInfo if hasattr(response.ExchangeInfoResults, 'ExchangeInfo') else []
                if not isinstance(items, list):
                    items = [items]
                for exchange_info in items:
                    print(f"Phone Number     : {getattr(exchange_info, 'PhoneNumber', '')}")
                    print(f"Name             : {getattr(exchange_info, 'Name', '')}")
                    print(f"City             : {getattr(exchange_info, 'City', '')}")
                    print(f"State            : {getattr(exchange_info, 'State', '')}")
                    print(f"Country          : {getattr(exchange_info, 'Country', '')}")
                    print(f"Line Type        : {getattr(exchange_info, 'LineType', '')}")
                    print(f"Time Zone        : {getattr(exchange_info, 'TimeZone', '')}")
                    print(f"Latitude         : {getattr(exchange_info, 'Latitude', '')}")
                    print(f"Longitude        : {getattr(exchange_info, 'Longitude', '')}")
                    print(f"SMS Address      : {getattr(exchange_info, 'SMSAddress', '')}")
                    print(f"MMS Address      : {getattr(exchange_info, 'MMSAddress', '')}")
                    print(f"Note Codes       : {getattr(exchange_info, 'NoteCodes', [])}")
                    print(f"Note Descriptions: {getattr(exchange_info, 'NoteDescriptions', [])}")

                    print("\r\n* Ported Info *\r\n")
                    if hasattr(exchange_info, 'PortedInfo') and exchange_info.PortedInfo:
                        print(f"Original Name     : {getattr(exchange_info.PortedInfo, 'OriginalName', '')}")
                        print(f"Original Line Type: {getattr(exchange_info.PortedInfo, 'OriginalLineType', '')}")
                        print(f"Ported Date       : {getattr(exchange_info.PortedInfo, 'PortedDate', '')}")
                        print(f"LATA              : {getattr(exchange_info.PortedInfo, 'LATA', '')}")
                    else:
                        print("No ported info found.")
            else:
                print("No exchange info items found.")
        else:
            print("No exchange info found.")

        if hasattr(response, 'Error') and response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Type    : {response.Error.Type}")
            print(f"Error Desc    : {response.Error.Desc}")
            print(f"Error TypeCode: {response.Error.TypeCode}")
            print(f"Error DescCode: {response.Error.DescCode}")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Exception occurred: {str(e)}")