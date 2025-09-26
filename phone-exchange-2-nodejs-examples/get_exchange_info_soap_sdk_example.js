import { GetExchangeInfoSoap } from '../phone-exchange-2-nodejs/SOAP/get_exchange_info_soap.js';

async function GetExchangeInfoSoapGo(licenseKey, isLive) {
    console.log("\n-------------------------------------------");
    console.log("PhoneExchange2 - GetExchangeInfo - SOAP SDK");
    console.log("-------------------------------------------");

    const phoneNumber = "+18059631700";
    const timeoutSeconds = 15;

    console.log("\n* Input *\n");
    console.log(`Phone Number   : ${phoneNumber}`);
    console.log(`License Key    : ${licenseKey}`);
    console.log(`Is Live        : ${isLive}`);
    console.log(`Timeout Seconds: ${timeoutSeconds}`);

    try {
        const pe2 = new GetExchangeInfoSoap(phoneNumber,licenseKey,isLive, timeoutSeconds);
        const response = await pe2.getExchangeInfoSoap();

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
    } catch (e) {
        console.log("\n* Error *\n");
        console.log(`Error Message: ${e.message}`);
    }
}

export { GetExchangeInfoSoapGo };