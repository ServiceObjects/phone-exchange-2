import sys
import os

sys.path.insert(0, os.path.abspath("../phone-exchange-2-python/REST"))

from get_exchange_info_rest import get_exchange_info


def get_exchange_info_rest_sdk_go(is_live: bool, license_key: str) -> None:
    print("\r\n------------------------------------------")
    print("PhoneExchange - GetExchangeInfo - REST SDK")
    print("------------------------------------------")

    phone_number = "805-963-1700"
    timeout_seconds = 10  

    print("\r\n* Input *\r\n")
    print(f"Phone Number   : {phone_number}")
    print(f"License Key    : {license_key}")
    print(f"Is Live        : {is_live}")
    print(f"Timeout Seconds: {timeout_seconds}")

    try:
        response = get_exchange_info(phone_number, license_key, is_live)

        print("\r\n* Exchange Info *\r\n")
        if response and not response.Error:
            if response.ExchangeInfoResults and len(response.ExchangeInfoResults) > 0:
                for exchange_info in response.ExchangeInfoResults:
                    print(f"Phone Number     : {exchange_info.PhoneNumber}")
                    print(f"Name             : {exchange_info.Name}")
                    print(f"City             : {exchange_info.City}")
                    print(f"State            : {exchange_info.State}")
                    print(f"Country          : {exchange_info.Country}")
                    print(f"Line Type        : {exchange_info.LineType}")
                    print(f"Time Zone        : {exchange_info.TimeZone}")
                    print(f"Latitude         : {exchange_info.Latitude}")
                    print(f"Longitude        : {exchange_info.Longitude}")
                    print(f"SMS Address      : {exchange_info.SMSAddress}")
                    print(f"MMS Address      : {exchange_info.MMSAddress}")
                    print(f"Note Codes       : {exchange_info.NoteCodes}")
                    print(f"Note Descriptions: {exchange_info.NoteDescriptions}")

                    print("\r\n* Ported Info *\r\n")
                    if exchange_info.PortedInfo:
                        print(f"Original Name     : {exchange_info.PortedInfo.OriginalName}")
                        print(f"Original Line Type: {exchange_info.PortedInfo.OriginalLineType}")
                        print(f"Ported Date       : {exchange_info.PortedInfo.PortedDate}")
                        print(f"LATA              : {exchange_info.PortedInfo.LATA}")
                    else:
                        print("No ported info found.")
            else:
                print("No exchange info items found.")
        else:
            print("No exchange info found.")

        if response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Type    : {response.Error.Type}")
            print(f"Error Desc    : {response.Error.Desc}")
            print(f"Error TypeCode: {response.Error.TypeCode}")
            print(f"Error DescCode: {response.Error.DescCode}")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Exception occurred: {str(e)}")