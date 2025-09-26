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
//               LicenseKey
//               IsLive
// 
// Optional:
//        PhoneNumber
//        TimeoutSeconds (default: 15)

using phone_exchange_2_dot_net.REST;

GetExchangeInfoClient.GetExchangeInfoInput getExchangeInfoInput = new(
    PhoneNumber: "805-963-1700",
    LicenseKey: licenseKey,
    IsLive: isLive,
    TimeoutSeconds: 15
);

// 2. Call the sync Invoke() method.
PE2Response response = GetExchangeInfoClient.Invoke(getExchangeInfoInput);

// 3. Inspect results.
if (response.Error is null)
{
    Console.WriteLine("\r\n* Exchange Info *\r\n");
    if (response.ExchangeInfoResults?.Length > 0)
    {
        foreach (var exchangeInfo in response.ExchangeInfoResults)
        {
            Console.WriteLine($"Phone Number     : {exchangeInfo.PhoneNumber}");
            Console.WriteLine($"Name             : {exchangeInfo.Name}");
            Console.WriteLine($"City             : {exchangeInfo.City}");
            Console.WriteLine($"State            : {exchangeInfo.State}");
            Console.WriteLine($"Country          : {exchangeInfo.Country}");
            Console.WriteLine($"Line Type        : {exchangeInfo.LineType}");
            Console.WriteLine($"Time Zone        : {exchangeInfo.TimeZone}");
            Console.WriteLine($"Latitude         : {exchangeInfo.Latitude}");
            Console.WriteLine($"Longitude        : {exchangeInfo.Longitude}");
            Console.WriteLine($"SMS Address      : {exchangeInfo.SMSAddress}");
            Console.WriteLine($"MMS Address      : {exchangeInfo.MMSAddress}");
            Console.WriteLine($"Note Codes       : {exchangeInfo.NoteCodes}");
            Console.WriteLine($"Note Descriptions: {exchangeInfo.NoteDescriptions}");

            Console.WriteLine("\r\n* Ported Info *\r\n");
            if (exchangeInfo.PortedInfo != null)
            {
                Console.WriteLine($"Original Name     : {exchangeInfo.PortedInfo.OriginalName}");
                Console.WriteLine($"Original Line Type: {exchangeInfo.PortedInfo.OriginalLineType}");
                Console.WriteLine($"Ported Date       : {exchangeInfo.PortedInfo.PortedDate}");
                Console.WriteLine($"LATA              : {exchangeInfo.PortedInfo.LATA}");
            }
            else
            {
                Console.WriteLine("No ported info found.");
            }
        }
    }
    else
    {
        Console.WriteLine("No exchange info items found.");
    }
}
else
{
    Console.WriteLine("\r\n* Error *\r\n");
    Console.WriteLine($"Error Type     : {response.Error.Type}");
    Console.WriteLine($"Error Type Code: {response.Error.TypeCode}");
    Console.WriteLine($"Error Desc     : {response.Error.Desc}");
    Console.WriteLine($"Error Desc Code: {response.Error.DescCode}");
}
```
# PE2 - GetInternationalExchangeInfo

Our international Phone Exchange service validates and formats phone numbers for international direct dialing, while returning line type, country code and geocoding information.

### [GetBestMatches_V4 Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-fasttax/ft-operations/ft-getbestmatch-recommended-operation/)

## Library Usage

```
// 1. Build the input
//
//  Required fields:
//               LicenseKey
//               IsLive
// 
// Optional:
//        PhoneNumber
//        Country
//        TimeoutSeconds (default: 15)

using phone_exchange_2_dot_net.REST;

GetInternationalExchangeInfoClient.GetInternationalExchangeInfoInput getInternationalExchangeInfoInput = new(
    PhoneNumber: "+18059631700",
    Country: "US",
    LicenseKey: licenseKey,
    IsLive: isLive,
    TimeoutSeconds: 15
);

// 2. Call the sync Invoke() method.
 PE2Response response = GetInternationalExchangeInfoClient.Invoke(getInternationalExchangeInfoInput);

// 3. Inspect results.
if (response.Error is null)
{
    Console.WriteLine("\r\n* International Exchange Info *\r\n");
    if (response.InternationalExchangeInfo != null)
    {
        Console.WriteLine($"Phone Number In     : {response.InternationalExchangeInfo.PhoneNumberIn}");
        Console.WriteLine($"Country Code        : {response.InternationalExchangeInfo.CountryCode}");
        Console.WriteLine($"Format National     : {response.InternationalExchangeInfo.FormatNational}");
        Console.WriteLine($"Extension           : {response.InternationalExchangeInfo.Extension}");
        Console.WriteLine($"Locality            : {response.InternationalExchangeInfo.Locality}");
        Console.WriteLine($"Locality Match Level: {response.InternationalExchangeInfo.LocalityMatchLevel}");
        Console.WriteLine($"Time Zone           : {response.InternationalExchangeInfo.TimeZone}");
        Console.WriteLine($"Latitude            : {response.InternationalExchangeInfo.Latitude}");
        Console.WriteLine($"Longitude           : {response.InternationalExchangeInfo.Longitude}");
        Console.WriteLine($"Country             : {response.InternationalExchangeInfo.Country}");
        Console.WriteLine($"Country ISO2        : {response.InternationalExchangeInfo.CountryISO2}");
        Console.WriteLine($"Country ISO3        : {response.InternationalExchangeInfo.CountryISO3}");
        Console.WriteLine($"Format International: {response.InternationalExchangeInfo.FormatInternational}");
        Console.WriteLine($"Format E164         : {response.InternationalExchangeInfo.FormatE164}");
        Console.WriteLine($"Carrier             : {response.InternationalExchangeInfo.Carrier}");
        Console.WriteLine($"Line Type           : {response.InternationalExchangeInfo.LineType}");
        Console.WriteLine($"SMS Address         : {response.InternationalExchangeInfo.SMSAddress}");
        Console.WriteLine($"MMS Address         : {response.InternationalExchangeInfo.MMSAddress}");
        Console.WriteLine($"Is Valid            : {response.InternationalExchangeInfo.IsValid}");
        Console.WriteLine($"Is Valid For Region : {response.InternationalExchangeInfo.IsValidForRegion}");
        Console.WriteLine($"Note Codes          : {response.InternationalExchangeInfo.NoteCodes}");
        Console.WriteLine($"Note Descriptions   : {response.InternationalExchangeInfo.NoteDescriptions}");
    }
    else
    {
        Console.WriteLine("No international exchange info items found.");
    }
}
else
{
    Console.WriteLine("\r\n* Error *\r\n");
    Console.WriteLine($"Error Type     : {response.Error.Type}");
    Console.WriteLine($"Error Type Code: {response.Error.TypeCode}");
    Console.WriteLine($"Error Desc     : {response.Error.Desc}");
    Console.WriteLine($"Error Desc Code: {response.Error.DescCode}");
}
```

