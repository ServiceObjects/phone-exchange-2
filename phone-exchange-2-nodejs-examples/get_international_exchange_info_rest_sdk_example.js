import { GetInternationalExchangeInfoClient } from '../phone-exchange-2-nodejs/REST/get_international_exchange_info_rest.js';

async function GetInternationalExchangeInfoRestGo(licenseKey, isLive) {
    console.log('\n--------------------------------------------------------');
    console.log('PhoneExchange2 - GetInternationalExchangeInfo - REST SDK');
    console.log('--------------------------------------------------------');

    const phoneNumber = '+18059631700';
    const country = 'US';
    const timeoutSeconds = 15;

    console.log('\n* Input *\n');
    console.log(`Phone Number   : ${phoneNumber}`);
    console.log(`Country        : ${country}`);
    console.log(`License Key    : ${licenseKey}`);
    console.log(`Is Live        : ${isLive}`);
    console.log(`Timeout Seconds: ${timeoutSeconds}`);

    try {
        const response = await GetInternationalExchangeInfoClient.invoke(phoneNumber, country, licenseKey, isLive, timeoutSeconds);

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
    } catch (error) {
        console.log('\n* Error *\n');
        console.log(`Error Message: ${error.message}`);
    }
}

export { GetInternationalExchangeInfoRestGo };