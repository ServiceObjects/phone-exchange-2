import {GetExchangeInfoRestGo} from'./get_exchange_info_rest_sdk_example.js';    
import {GetExchangeInfoSoapGo} from './get_exchange_info_soap_sdk_example.js'
import {GetInternationalExchangeInfoRestGo} from './get_international_exchange_info_rest_sdk_example.js'
import {GetInternationalExchangeInfoSoapGo} from './get_international_exchange_info_soap_sdk_example .js'

export async function main() {
//Your license key from Service Objects.
//Trial license keys will only work on the
//trail environments and production license
//keys will only work on production environments.
const licenseKey = "LICENSE KEY";
const isLive = true; 

// PhoneExchange2 - GetExchangeInfo - REST SDK
await GetExchangeInfoRestGo(licenseKey, isLive);

// PhoneExchange2 - GetExchangeInfo - SOAP SDK
await GetExchangeInfoSoapGo(licenseKey, isLive);

// PhoneExchange2 - GetInternationalExchangeInfo - REST SDK
await GetInternationalExchangeInfoRestGo(licenseKey, isLive);

// PhoneExchange2 - GetInternationalExchangeInfo - SOAP SDK
await GetInternationalExchangeInfoSoapGo(licenseKey, isLive);

}
main().catch(console.error) ;