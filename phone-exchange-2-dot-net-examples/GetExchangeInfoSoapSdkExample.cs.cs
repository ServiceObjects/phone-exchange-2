using PE2Reference;
using phone_exchange_2_dot_net.SOAP;

namespace phone_exchange_2_dot_net_examples
{
    public static class GetExchangeInfoSoapSdkExample
    {
        public static void Go(string licenseKey, bool isLive)
        {
            Console.WriteLine("\r\n-------------------------------------------");
            Console.WriteLine("PhoneExchange2 - GetExchangeInfo - SOAP SDK");
            Console.WriteLine("-------------------------------------------");

            string PhoneNumber = "805-963-1700";

            Console.WriteLine("\r\n* Input *\r\n");
            Console.WriteLine($"Phone Number  : {PhoneNumber}");
            Console.WriteLine($"License Key   : {licenseKey}");
            Console.WriteLine($"Is Live       : {isLive}");

            var pe2 = new GetExchangeInfoValidation(isLive);
            ExchangeInfoResponse response = pe2.GetExchangeInfo(PhoneNumber, licenseKey).Result;

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
        }
    }
}