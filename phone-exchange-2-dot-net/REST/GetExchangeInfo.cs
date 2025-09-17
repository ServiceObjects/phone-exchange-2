
using System.Web;

namespace phone_exchange_2_dot_net.REST
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects Phone Exchange (PE2) REST API's GetExchangeInfo endpoint,
    /// retrieving phone exchange information (e.g., carrier, line type, ported status) for a given phone number
    /// with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public static class GetExchangeInfoClient
    {
        // Base URL constants: production, backup, and trial
        private const string LiveBaseUrl = "https://sws.serviceobjects.com/pe2/web.svc/json/";
        private const string BackupBaseUrl = "https://swsbackup.serviceobjects.com/pe2/web.svc/json/";
        private const string TrialBaseUrl = "https://trial.serviceobjects.com/pe2/web.svc/json/";

        /// <summary>
        /// Synchronously calls the GetExchangeInfo REST endpoint to retrieve phone exchange information,
        /// attempting the primary endpoint first and falling back to the backup if the response is invalid
        /// (Error.TypeCode == "3") in live mode.
        /// </summary>
        /// <param name="input">The input parameters including phone number, country code, and license key.</param>
        /// <returns>Deserialized <see cref="PE2Response"/> containing phone exchange data or an error.</returns>
        public static PE2Response Invoke(GetExchangeInfoInput input)
        {
            // Use query string parameters so missing/optional fields don't break the URL
            string url = BuildUrl(input, input.IsLive ? LiveBaseUrl : TrialBaseUrl);
            PE2Response response = Helper.HttpGet<PE2Response>(url, input.TimeoutSeconds);

            // Fallback on error in live mode
            if (input.IsLive && !IsValid(response))
            {
                string fallbackUrl = BuildUrl(input, BackupBaseUrl);
                PE2Response fallbackResponse = Helper.HttpGet<PE2Response>(fallbackUrl, input.TimeoutSeconds);
                return fallbackResponse;
            }

            return response;
        }

        /// <summary>
        /// Asynchronously calls the GetExchangeInfo REST endpoint to retrieve phone exchange information,
        /// attempting the primary endpoint first and falling back to the backup if the response is invalid
        /// (Error.TypeCode == "3") in live mode.
        /// </summary>
        /// <param name="input">The input parameters including phone number, country code, and license key.</param>
        /// <returns>Deserialized <see cref="PE2Response"/> containing phone exchange data or an error.</returns>
        public static async Task<PE2Response> InvokeAsync(GetExchangeInfoInput input)
        {
            // Use query string parameters so missing/optional fields don't break the URL
            string url = BuildUrl(input, input.IsLive ? LiveBaseUrl : TrialBaseUrl);
            PE2Response response = await Helper.HttpGetAsync<PE2Response>(url, input.TimeoutSeconds).ConfigureAwait(false);

            // Fallback on error in live mode
            if (input.IsLive && !IsValid(response))
            {
                string fallbackUrl = BuildUrl(input, BackupBaseUrl);
                PE2Response fallbackResponse = await Helper.HttpGetAsync<PE2Response>(fallbackUrl, input.TimeoutSeconds).ConfigureAwait(false);
                return fallbackResponse;
            }

            return response;
        }

        // Build the full request URL, including URL-encoded query string
        public static string BuildUrl(GetExchangeInfoInput input, string baseUrl)
        {
            // Construct query string with URL-encoded parameters
            string qs = $"GetExchangeInfo?" +
                        $"PhoneNumber={Helper.UrlEncode(input.PhoneNumber)}" +
                        $"&CountryCode={Helper.UrlEncode(input.CountryCode)}" +
                        $"&Country={Helper.UrlEncode(input.Country)}" +
                        $"&IPAddress={Helper.UrlEncode(input.IPAddress)}" +
                        $"&CallerCountry={Helper.UrlEncode(input.CallerCountry)}" +
                        $"&Extras={Helper.UrlEncode(input.Extras)}" +
                        $"&Token={Helper.UrlEncode(input.Token)}" +
                        $"&LicenseKey={Helper.UrlEncode(input.LicenseKey)}";
            return baseUrl + qs;
        }

        private static bool IsValid(PE2Response response) => response?.Error == null || response.Error.TypeCode != "3";

        /// <summary>
        /// Input parameters for the GetExchangeInfo API call. Represents a phone number to retrieve exchange information.
        /// </summary>
        /// <param name="PhoneNumber">The phone number to validate (e.g., "1234567890").</param>
        /// <param name="CountryCode">1-3 digit country calling code (e.g., "1"). Optional.</param>
        /// <param name="Country">ISO2, ISO3, or country name (e.g., "US"). Optional.</param>
        /// <param name="IPAddress">IPv4 address. Optional.</param>
        /// <param name="CallerCountry">ISO2 or ISO3 code representing the caller's country. Optional.</param>
        /// <param name="Extras">Comma-separated list of possible options. Optional.</param>
        /// <param name="LicenseKey">The license key to authenticate the API request.</param>
        /// <param name="IsLive">Indicates whether to use the live service (true) or trial service (false).</param>
        /// <param name="TimeoutSeconds">Timeout duration for the API call, in seconds.</param>
        public record GetExchangeInfoInput(
            string PhoneNumber = "",
            string CountryCode = "",
            string Country = "",
            string IPAddress = "",
            string CallerCountry = "",
            string Extras = "",
            string LicenseKey = "",
            string Token = "",
            bool IsLive = true,
            int TimeoutSeconds = 15
        );
    }
}