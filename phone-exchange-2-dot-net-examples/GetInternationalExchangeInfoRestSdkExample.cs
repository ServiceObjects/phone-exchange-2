using phone_exchange_2_dot_net.REST;

namespace phone_exchange_2_dot_net_examples
{
    public class GetInternationalExchangeInfoRestSdkExample
    {
        public static void Go(string licenseKey, bool isLive)
        {
            Console.WriteLine("\r\n--------------------------------------------------------");
            Console.WriteLine("PhoneExchange2 - GetInternationalExchangeInfo - REST SDK");
            Console.WriteLine("--------------------------------------------------------");

            GetInternationalExchangeInfoClient.GetInternationalExchangeInfoInput getInternationalExchangeInfoInput = new(
                PhoneNumber: "+12025550123",
                Country: "US",
                LicenseKey: licenseKey,
                IsLive: isLive,
                TimeoutSeconds: 15
            );

            Console.WriteLine("\r\n* Input *\r\n");
            Console.WriteLine($"Phone Number: {getInternationalExchangeInfoInput.PhoneNumber}");
            Console.WriteLine($"Country     : {getInternationalExchangeInfoInput.Country}");
            Console.WriteLine($"License Key : {getInternationalExchangeInfoInput.LicenseKey}");
            Console.WriteLine($"Is Live     : {getInternationalExchangeInfoInput.IsLive}");

            PE2Response response = GetInternationalExchangeInfoClient.Invoke(getInternationalExchangeInfoInput);
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
        }
    }
}