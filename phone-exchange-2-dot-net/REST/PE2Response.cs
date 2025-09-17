using System.Runtime.Serialization;
using System.Linq;

namespace phone_exchange_2_dot_net.REST
{
    /// <summary>
    /// Response from PE2 GetExchangeInfo and GetInternationalExchangeInfo APIs, containing phone exchange information.
    /// </summary>
    [DataContract]
    public class PE2Response
    {
        public ExchangeInfo[] ExchangeInfoResults { get; set; }
        public InternationalExchangeInfo InternationalExchangeInfo { get; set; }
        public Error Error { get; set; }

        public override string ToString()
        {
            string exchangeInfoStr = ExchangeInfoResults != null
                ? string.Join("\n", ExchangeInfoResults.Select(r => r.ToString()))
                : "null";
            string internationalInfoStr = InternationalExchangeInfo != null
                ? InternationalExchangeInfo.ToString()
                : "";
            return $"PE2Response:\n" +
                   $"ExchangeInfoResults:\n{exchangeInfoStr}\n" +
                   $"InternationalExchangeInfo:\n{internationalInfoStr}\n" +
                   $"Error: {(Error != null ? Error.ToString() : "null")}";
        }
    }

    /// <summary>
    /// Phone exchange information for a validated phone number (USA/Canada).
    /// </summary>
    [DataContract]
    public class ExchangeInfo
    {
        public string PhoneNumber { get; set; }
        public string Name { get; set; }
        public string City { get; set; }
        public string State { get; set; }
        public string Country { get; set; }
        public string LineType { get; set; }
        public string TimeZone { get; set; }
        public string Latitude { get; set; }
        public string Longitude { get; set; }
        public string SMSAddress { get; set; }
        public string MMSAddress { get; set; }
        public PortedInfo PortedInfo { get; set; }
        public string NoteCodes { get; set; }
        public string NoteDescriptions { get; set; }

        public override string ToString()
        {
            string portedInfoStr = PortedInfo != null
                ? PortedInfo.ToString()
                : "";
            return $"ExchangeInfo:\n" +
                   $"PhoneNumber: {PhoneNumber}\n" +
                   $"Name: {Name}\n" +
                   $"City: {City}\n" +
                   $"State: {State}\n" +
                   $"Country: {Country}\n" +
                   $"LineType: {LineType}\n" +
                   $"TimeZone: {TimeZone}\n" +
                   $"Latitude: {Latitude}\n" +
                   $"Longitude: {Longitude}\n" +
                   $"SMSAddress: {SMSAddress}\n" +
                   $"MMSAddress: {MMSAddress}\n" +
                   $"PortedInfo: {portedInfoStr}\n" +
                   $"NoteCodes: {NoteCodes}\n" +
                   $"NoteDescriptions: {NoteDescriptions}";
        }
    }

    /// <summary>
    /// Ported information for a phone number.
    /// </summary>
    [DataContract]
    public class PortedInfo
    {
        public string OriginalName { get; set; }
        public string OriginalLineType { get; set; }
        public string PortedDate { get; set; }
        public string LATA { get; set; }

        public override string ToString()
        {
            return $"OriginalName: {OriginalName}, OriginalLineType: {OriginalLineType}, PortedDate: {PortedDate}, LATA: {LATA}";
        }
    }

    /// <summary>
    /// International phone exchange information for a validated phone number.
    /// </summary>
    [DataContract]
    public class InternationalExchangeInfo
    {
        public string PhoneNumberIn { get; set; }
        public string CountryCode { get; set; }
        public string FormatNational { get; set; }
        public string Extension { get; set; }
        public string Locality { get; set; }
        public string LocalityMatchLevel { get; set; }
        public string TimeZone { get; set; }
        public string Latitude { get; set; }
        public string Longitude { get; set; }
        public string Country { get; set; }
        public string CountryISO2 { get; set; }
        public string CountryISO3 { get; set; }
        public string FormatInternational { get; set; }
        public string FormatE164 { get; set; }
        public string Carrier { get; set; }
        public string LineType { get; set; }
        public string SMSAddress { get; set; }
        public string MMSAddress { get; set; }
        public bool IsValid { get; set; }
        public bool IsValidForRegion { get; set; }
        public string NoteCodes { get; set; }
        public string NoteDescriptions { get; set; }

        public override string ToString()
        {
            return $"InternationalExchangeInfo:\n" +
                   $"PhoneNumberIn: {PhoneNumberIn}\n" +
                   $"CountryCode: {CountryCode}\n" +
                   $"FormatNational: {FormatNational}\n" +
                   $"Extension: {Extension}\n" +
                   $"Locality: {Locality}\n" +
                   $"LocalityMatchLevel: {LocalityMatchLevel}\n" +
                   $"TimeZone: {TimeZone}\n" +
                   $"Latitude: {Latitude}\n" +
                   $"Longitude: {Longitude}\n" +
                   $"Country: {Country}\n" +
                   $"CountryISO2: {CountryISO2}\n" +
                   $"CountryISO3: {CountryISO3}\n" +
                   $"FormatInternational: {FormatInternational}\n" +
                   $"FormatE164: {FormatE164}\n" +
                   $"Carrier: {Carrier}\n" +
                   $"LineType: {LineType}\n" +
                   $"SMSAddress: {SMSAddress}\n" +
                   $"MMSAddress: {MMSAddress}\n" +
                   $"IsValid: {IsValid}\n" +
                   $"IsValidForRegion: {IsValidForRegion}\n" +
                   $"NoteCodes: {NoteCodes}\n" +
                   $"NoteDescriptions: {NoteDescriptions}";
        }
    }

    /// <summary>
    /// Error object for PE2 API responses.
    /// </summary>
    [DataContract]
    public class Error
    {
        public string Type { get; set; }
        public string Desc { get; set; }
        public string TypeCode { get; set; }
        public string DescCode { get; set; }

        public override string ToString()
        {
            return $"Desc: {Desc}, TypeCode: {TypeCode}, DescCode: {DescCode}, Type: {Type}";
        }
    }
}