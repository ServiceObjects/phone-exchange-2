using phone_exchange_2_dot_net_examples;

//Your license key from Service Objects.
//Trial license keys will only work on the
//trail environments and production license
//keys will only work on production environments.
string LicenseKey = "LICENSE KEY";

bool IsProductionKey = true;

// PhoneExchange2 - GetExchangeInfo - REST SDK
GetExchangeInfoRestSdkExample.Go(LicenseKey, IsProductionKey);

// PhoneExchange2 - GetExchangeInfo - SOAP SDK
GetExchangeInfoSoapSdkExample.Go(LicenseKey, IsProductionKey);

// PhoneExchange2 - GetInternationalExchangeInfo - REST SDK
GetInternationalExchangeInfoRestSdkExample.Go(LicenseKey, IsProductionKey);

// PhoneExchange2 - GetInternationalExchangeInfo - SOAP SDK
GetInternationalExchangeInfoSoapSdkExample.Go(LicenseKey, IsProductionKey);
