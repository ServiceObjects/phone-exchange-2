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
//               licenseKey
//               isLive
// 
// Optional:
//        phoneNumber
//        timeoutSeconds (default: 15)

import { GetExchangeInfoSoap } from '../phone-exchange-2-nodejs/SOAP/get_exchange_info_soap.js';

const phoneNumber = '+18059631700';
const timeoutSeconds = 15;
const isLive = false;
const licenseKey = 'YOUR LICENSE KEY';

// 2. Call the sync Invoke() method.
const pe2 = new GetExchangeInfoSoap(phoneNumber,licenseKey,isLive, timeoutSeconds);
const response = await pe2.getExchangeInfoSoap();

// 3. Inspect results.
console.log("\n* Exchange Info *\n");
if (response.Error) {
    console.log("\n* Error *\n");
    console.log(`Error Type    : ${response.Error.Type}`);
    console.log(`Error Desc    : ${response.Error.Desc}`);
    console.log(`Error TypeCode: ${response.Error.TypeCode}`);
    console.log(`Error DescCode: ${response.Error.DescCode}`);
}

if (response.ExchangeInfoResults) {
    console.log(`Phone Number     : ${response.ExchangeInfoResults.ExchangeInfo[0].PhoneNumber}`);
    console.log(`Carrier Name     : ${response.ExchangeInfoResults.ExchangeInfo[0].Name}`);
    console.log(`City             : ${response.ExchangeInfoResults.ExchangeInfo[0].City}`);
    console.log(`State            : ${response.ExchangeInfoResults.ExchangeInfo[0].State}`);
    console.log(`Country          : ${response.ExchangeInfoResults.ExchangeInfo[0].Country}`);
    console.log(`Line Type        : ${response.ExchangeInfoResults.ExchangeInfo[0].LineType}`);
    console.log(`Time Zone        : ${response.ExchangeInfoResults.ExchangeInfo[0].TimeZone}`);
    console.log(`Latitude         : ${response.ExchangeInfoResults.ExchangeInfo[0].Latitude}`);
    console.log(`Longitude        : ${response.ExchangeInfoResults.ExchangeInfo[0].Longitude}`);
    console.log(`SMS Address      : ${response.ExchangeInfoResults.ExchangeInfo[0].SMSAddress}`);
    console.log(`MMS Address      : ${response.ExchangeInfoResults.ExchangeInfo[0].MMSAddress}`);
    console.log(`Note Codes       : ${response.ExchangeInfoResults.ExchangeInfo[0].NoteCodes}`);
    console.log(`Note Descriptions: ${response.ExchangeInfoResults.ExchangeInfo[0].NoteDescriptions}`);

    console.log("\n* Ported Info *\n");
    if (response.ExchangeInfoResults.ExchangeInfo[0].PortedInfo) {
        console.log(`Original Carrier Name: ${response.ExchangeInfoResults.ExchangeInfo[0].PortedInfo.OriginalName}`);
        console.log(`Original Line Type   : ${response.ExchangeInfoResults.ExchangeInfo[0].PortedInfo.OriginalLineType}`);
        console.log(`Ported Date          : ${response.ExchangeInfoResults.ExchangeInfo[0].PortedInfo.PortedDate}`);
        console.log(`LATA                 : ${response.ExchangeInfoResults.ExchangeInfo[0].PortedInfo.LATA}`);
    } else {
        console.log("No ported info found.");
    }
} else {
    console.log("No exchange info results found.");
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
//               licenseKey
//               isLive
// 
// Optional:
//        phoneNumber
//        country
//        timeoutSeconds (default: 15)

import { GetInternationalExchangeInfoSoap } from '../phone-exchange-2-nodejs/SOAP/get_international_exchange_info_soap.js';

const phoneNumber = '+12025550123';
const country = 'US';
const timeoutSeconds = 15;
const isLive = false;
const licenseKey = 'YOUR LICENSE KEY';

// 2. Call the sync Invoke() method.
const pe2 = new GetInternationalExchangeInfoSoap(phoneNumber,country,licenseKey,isLive,timeoutSeconds);
const response = await pe2.getInternationalExchangeInfoSoap();

// 3. Inspect results.
console.log("\n* International Exchange Info *\n");
if (response.Error) {
    console.log("\n* Error *\n");
    console.log(`Error Type    : ${response.Error.Type}`);
    console.log(`Error Desc    : ${response.Error.Desc}`);
    console.log(`Error TypeCode: ${response.Error.TypeCode}`);
    console.log(`Error DescCode: ${response.Error.DescCode}`);
}

if (response.InternationalExchangeInfo) {
    console.log(`Phone Number In     : ${response.InternationalExchangeInfo.NumberIn}`);
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
    console.log("No international exchange info results found.");
}
```

