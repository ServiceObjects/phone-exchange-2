![Service Objects Logo](https://www.serviceobjects.com/wp-content/uploads/2021/05/SO-Logo-with-TM.gif "Service Objects Logo")

# PE2 - Phone Exchange 2

DOTS FastTax (referred to as FastTax or FT) is a publicly available XML and JSON web service that provides sales tax rate information for all US areas based on several different inputs. The service provides zip, city, county, county fips codes, state, tax rates and exemptions. 

Our international Phone Exchange service validates and formats phone numbers for international direct dialing, while returning line type, country code and geocoding information.

## [Service Objects Website](https://serviceobjects.com)

# PE2 - GetExchangeInfo

Our domestic (USA/Canada) Phone Exchange service returns comprehensive carrier and exchange information, including ported status, SMS and MMS details and identifies high-risk VOIP and prepay phones.

### [GetBestMatches_V4 Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-fasttax/ft-operations/ft-getbestmatch-recommended-operation/)

## Library Usage

```
// 1. Build the input
//
//  Required fields:
//               license_key
//               is_live
// 
// Optional:
//        phone_number
//        timeout_seconds (default: 15)

from get_exchange_info_soap import GetExchangeInfoSoap

phone_number = "805-963-1700"
timeout_seconds = 15
is_live = False
license_key = "YOUR LICENSE KEY"

// 2. Call the method.
service = GetExchangeInfoSoap(license_key, is_live, timeout_seconds * 1000)
response = service.get_exchange_info(phone_number)

// 3. Inspect results.
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
```
# PE2 - GetInternationalExchangeInfo

Our international Phone Exchange service validates and formats phone numbers for international direct dialing, while returning line type, country code and geocoding information.

### [GetBestMatches_V4 Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-fasttax/ft-operations/ft-getbestmatch-recommended-operation/)

## Library Usage

```
// 1. Build the input
//
//  Required fields:
//               license_key
//               is_live
// 
// Optional:
//        phone_number
//        country
//        timeout_seconds (default: 15)

from get_international_exchange_info_soap import GetInternationalExchangeInfoSoap

phone_number = "+18059631700"
country = "US"
timeout_seconds = 15
is_live = False
license_key = "YOUR LICENSE KEY"

// 2. Call the sync Invoke() method.
service = GetInternationalExchangeInfoSoap(license_key, is_live, timeout_seconds * 1000)
response = service.get_international_exchange_info(phone_number, country)

// 3. Inspect results.
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
```

