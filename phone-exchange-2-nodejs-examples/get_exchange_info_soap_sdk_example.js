import { GetExchangeInfoSoap } from '../phone-exchange-2-nodejs/SOAP/get_exchange_info_soap.js';

async function GetExchangeInfoSoapGo(licenseKey, isLive) {
    console.log("\n-------------------------------------------");
    console.log("PhoneExchange2 - GetExchangeInfo - SOAP SDK");
    console.log("-------------------------------------------");

    const phoneNumber = "8055551234";
    const timeoutSeconds = 15;

    console.log("\n* Input *\n");
    console.log(`Phone Number   : ${phoneNumber}`);
    console.log(`License Key    : ${licenseKey}`);
    console.log(`Is Live        : ${isLive}`);
    console.log(`Timeout Seconds: ${timeoutSeconds}`);

    try {
        const pe2 = new GetExchangeInfoSoap(
            phoneNumber,
            licenseKey,
            isLive,
            timeoutSeconds
        );
        const response = await pe2.invokeAsync();

        console.log("\n* Exchange Info *\n");
        if (response.Error) {
            console.log("\n* Error *\n");
            console.log(`Error Type    : ${response.Error.Type}`);
            console.log(`Error Desc    : ${response.Error.Desc}`);
            console.log(`Error TypeCode: ${response.Error.TypeCode}`);
            console.log(`Error DescCode: ${response.Error.DescCode}`);
        }

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

                console.log("\n* Ported Info *\n");
                if (exchangeInfo.PortedInfo) {
                    console.log(`Original Carrier Name: ${exchangeInfo.PortedInfo.OriginalName}`);
                    console.log(`Original Line Type   : ${exchangeInfo.PortedInfo.OriginalLineType}`);
                    console.log(`Ported Date          : ${exchangeInfo.PortedInfo.PortedDate}`);
                    console.log(`LATA                 : ${exchangeInfo.PortedInfo.LATA}`);
                } else {
                    console.log("No ported info found.");
                }
            }
        } else {
            console.log("No exchange info results found.");
        }
    } catch (e) {
        console.log("\n* Error *\n");
        console.log(`Error Message: ${e.message}`);
    }
}

export { GetExchangeInfoSoapGo };