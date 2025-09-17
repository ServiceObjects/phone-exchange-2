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
//        CountryCode
//        Country
//        IP Address
//        CallerCountry
//        Extras	
//        Token
//        TimeoutSeconds (default: 15)

import { GetExchangeInfoClient } from '../phone-exchange-2-nodejs/REST/get_exchange_info_rest.js';

const phoneNumber = '8055551234';
const countryCode = '1';
const country = 'US';
const ipAddress = '';
const callerCountry = '';
const extras = '';
const token = '';
const timeoutSeconds = 15;

// 2. Call the sync Invoke() method.
const response = await GetExchangeInfoClient.invoke(
    phoneNumber,
    countryCode,
    country,
    ipAddress,
    callerCountry,
    extras,
    token
    licenseKey,
    isLive,
    timeoutSeconds
);

// 3. Inspect results.
if (response.Error) {
    console.log('\n* Error *\n');
    console.log(`Error Type    : ${response.Error.Type}`);
    console.log(`Error DescCode: ${response.Error.DescCode}`);
    console.log(`Error Desc    : ${response.Error.Desc}`);
    console.log(`Error TypeCode: ${response.Error.TypeCode}`);
}

console.log('\n* Exchange Info *\n');
if (response.ExchangeInfoResults && response.ExchangeInfoResults.length > 0) {
    for (const exchangeInfo of response.ExchangeInfoResults) {
        console.log(`Phone Number     : ${exchangeInfo.PhoneNumber}`);
        console.log(`Carrier Name     : ${exchangeInfo.Name}`);
        console.log(`City             : ${exchangeInfo.City}`);
        console.log(`State            : ${exchangeInfo.State}`);
        console.log(`Country          : ${exchangeInfo.Country}`);
        console.log(`Line Type        : ${exchangeInfo.LineType}`);
        console.log(`Time Zone        : ${exchangeInfo.TimeZone}`);
        console.log(`Latitude         : ${exchangeInfo.Latitude}`);
        console.log(`Longitude        : ${exchangeInfo.Longitude}`);
        console.log(`SMS Address      : ${exchangeInfo.SMSAddress}`);
        console.log(`MMS Address      : ${exchangeInfo.MMSAddress}`);
        console.log(`Note Codes       : ${exchangeInfo.NoteCodes}`);
        console.log(`Note Descriptions: ${exchangeInfo.NoteDescriptions}`);

        console.log('\n* Ported Info *\n');
        if (exchangeInfo.PortedInfo) {
            console.log(`Original Carrier Name: ${exchangeInfo.PortedInfo.OriginalName}`);
            console.log(`Original Line Type   : ${exchangeInfo.PortedInfo.OriginalLineType}`);
            console.log(`Ported Date          : ${exchangeInfo.PortedInfo.PortedDate}`);
            console.log(`LATA                 : ${exchangeInfo.PortedInfo.LATA}`);
        } else {
            console.log('No ported info found.');
        }
    }
} else {
    console.log('No exchange info results found.');
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

import { GetInternationalExchangeInfoClient } from '../phone-exchange-2-nodejs/REST/get_international_exchange_info_rest.js';

const phoneNumber = '+12025550123';
const country = 'US';
const timeoutSeconds = 15;

// 2. Call the sync Invoke() method.
const response = await GetInternationalExchangeInfoClient.invoke(
    phoneNumber,
    country,
    licenseKey,
    isLive,
    timeoutSeconds
);

// 3. Inspect results.
if (response.Error) {
    console.log('\n* Error *\n');
    console.log(`Error Type    : ${response.Error.Type}`);
    console.log(`Error Desc    : ${response.Error.Desc}`);
    console.log(`Error TypeCode: ${response.Error.TypeCode}`);
    console.log(`Error DescCode: ${response.Error.DescCode}`);
}

console.log('\n* International Exchange Info *\n');
if (response.InternationalExchangeInfo) {
    console.log(`Phone Number In     : ${response.InternationalExchangeInfo.PhoneNumberIn}`);
    console.log(`Country Code        : ${response.InternationalExchangeInfo.CountryCode}`);
    console.log(`Format National     : ${response.InternationalExchangeInfo.FormatNational}`);
    console.log(`Extension           : ${response.InternationalExchangeInfo.Extension}`);
    console.log(`Locality            : ${response.InternationalExchangeInfo.Locality}`);
    console.log(`Locality Match Level: ${response.InternationalExchangeInfo.LocalityMatchLevel}`);
    console.log(`Time Zone           : ${response.InternationalExchangeInfo.TimeZone}`);
    console.log(`Latitude            : ${response.InternationalExchangeInfo.Latitude}`);
    console.log(`Longitude           : ${response.InternationalExchangeInfo.Longitude}`);
    console.log(`Country             : ${response.InternationalExchangeInfo.Country}`);
    console.log(`Country ISO2        : ${response.InternationalExchangeInfo.CountryISO2}`);
    console.log(`Country ISO3        : ${response.InternationalExchangeInfo.CountryISO3}`);
    console.log(`Format International: ${response.InternationalExchangeInfo.FormatInternational}`);
    console.log(`Format E164         : ${response.InternationalExchangeInfo.FormatE164}`);
    console.log(`Carrier             : ${response.InternationalExchangeInfo.Carrier}`);
    console.log(`Line Type           : ${response.InternationalExchangeInfo.LineType}`);
    console.log(`SMS Address         : ${response.InternationalExchangeInfo.SMSAddress}`);
    console.log(`MMS Address         : ${response.InternationalExchangeInfo.MMSAddress}`);
    console.log(`Is Valid            : ${response.InternationalExchangeInfo.IsValid}`);
    console.log(`Is Valid For Region : ${response.InternationalExchangeInfo.IsValidForRegion}`);
    console.log(`Note Codes          : ${response.InternationalExchangeInfo.NoteCodes}`);
    console.log(`Note Descriptions   : ${response.InternationalExchangeInfo.NoteDescriptions}`);
} else {
    console.log('No international exchange info results found.');
}
```

