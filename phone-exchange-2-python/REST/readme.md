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
//        phone__number
//        timeout_seconds (default: 15)

from get_exchange_info_rest import get_exchange_info

license_key = "8059631700"
timeout_seconds = 15
is_live = False
license_key = "YOUR LICENSE KEY"

// 2. Call the method.
response = get_exchange_info(phone_number, license_key, is_live)

// 3. Inspect results.
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

from get_international_exchange_info_rest import get_international_exchange_info

phone_number = "+18059631700"
country = "US"
timeout_seconds = 15
license_key = "YOUR LICENSE KEY"

// 2. Call the sync Invoke() method.
response = get_international_exchange_info(phone_number, country, license_key, is_live)

// 3. Inspect results.
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
```

