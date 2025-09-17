using PE2Reference;
using phone_exchange_2_dot_net.SOAP;

namespace phone_exchange_2_dot_net_examples
{
    public static class GetInternationalExchangeInfoSoapSdkExample
    {
        public static void Go(string licenseKey, bool isLive)
        {
            Console.WriteLine("\r\n--------------------------------------------------------");
            Console.WriteLine("PhoneExchange2 - GetInternationalExchangeInfo - SOAP SDK");
            Console.WriteLine("--------------------------------------------------------");

            string PhoneNumber = "+12025550123";
            string Country = "US";

            Console.WriteLine("\r\n* Input *\r\n");
            Console.WriteLine($"Phone Number  : {PhoneNumber}");
            Console.WriteLine($"Country       : {Country}");
            Console.WriteLine($"License Key   : {licenseKey}");
            Console.WriteLine($"Is Live       : {isLive}");

            var pe2 = new GetInternationalExchangeInfoValidation(isLive);
            InternationalExchangeInfoResponse response = pe2.GetInternationalExchangeInfo(PhoneNumber, Country, licenseKey).Result;

            if (response.Error is null)
            {
                Console.WriteLine("\r\n* International Exchange Info *\r\n");
                if (response.InternationalExchangeInfo != null)
                {
                    var exchangeInfo = response.InternationalExchangeInfo;
                    Console.WriteLine($"Phone Number In     : {exchangeInfo.NumberIn}");
                    Console.WriteLine($"Country Code        : {exchangeInfo.CountryCode}");
                    Console.WriteLine($"Format National     : {exchangeInfo.FormatNational}");
                    Console.WriteLine($"Extension           : {exchangeInfo.Extension}");
                    Console.WriteLine($"Locality            : {exchangeInfo.Locality}");
                    Console.WriteLine($"Locality Match Level: {exchangeInfo.LocalityMatchLevel}");
                    Console.WriteLine($"Time Zone           : {exchangeInfo.TimeZone}");
                    Console.WriteLine($"Latitude            : {exchangeInfo.Latitude}");
                    Console.WriteLine($"Longitude           : {exchangeInfo.Longitude}");
                    Console.WriteLine($"Country             : {exchangeInfo.Country}");
                    Console.WriteLine($"Country ISO2        : {exchangeInfo.CountryISO2}");
                    Console.WriteLine($"Country ISO3        : {exchangeInfo.CountryISO3}");
                    Console.WriteLine($"Format International: {exchangeInfo.FormatInternational}");
                    Console.WriteLine($"Format E164         : {exchangeInfo.FormatE164}");
                    Console.WriteLine($"Carrier             : {exchangeInfo.Carrier}");
                    Console.WriteLine($"Line Type           : {exchangeInfo.LineType}");
                    Console.WriteLine($"SMS Address         : {exchangeInfo.SMSAddress}");
                    Console.WriteLine($"MMS Address         : {exchangeInfo.MMSAddress}");
                    Console.WriteLine($"Is Valid            : {exchangeInfo.IsValid}");
                    Console.WriteLine($"Is Valid For Region : {exchangeInfo.IsValidForRegion}");
                    Console.WriteLine($"Note Codes          : {exchangeInfo.NoteCodes}");
                    Console.WriteLine($"Note Descriptions   : {exchangeInfo.NoteDescriptions}");
                }
                else
                {
                    Console.WriteLine("No international exchange info found.");
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
        }
    }
}