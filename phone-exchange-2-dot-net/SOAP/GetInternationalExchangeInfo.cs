using PE2Reference;

namespace phone_exchange_2_dot_net.SOAP
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects Phone Exchange (PE2) SOAP service's GetInternationalExchangeInfo operation,
    /// retrieving international phone exchange information (e.g., carrier, line type, formatted numbers) for a given phone number
    /// with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public class GetInternationalExchangeInfoValidation
    {
        private const string LiveBaseUrl = "https://sws.serviceobjects.com/pe2/soap.svc/SOAP";
        private const string BackupBaseUrl = "https://swsbackup.serviceobjects.com/pe2/soap.svc/SOAP";
        private const string TrialBaseUrl = "https://trial.serviceobjects.com/pe2/soap.svc/SOAP";

        private readonly string _primaryUrl;
        private readonly string _backupUrl;
        private readonly int _timeoutMs;
        private readonly bool _isLive;

        /// <summary>
        /// Initializes URLs/timeout/IsLive.
        /// </summary>
        public GetInternationalExchangeInfoValidation(bool isLive)
        {
            _timeoutMs = 10000;
            _isLive = isLive;

            _primaryUrl = isLive ? LiveBaseUrl : TrialBaseUrl;
            _backupUrl = isLive ? BackupBaseUrl : TrialBaseUrl;

            if (string.IsNullOrWhiteSpace(_primaryUrl))
                throw new InvalidOperationException("Primary URL not set.");
            if (string.IsNullOrWhiteSpace(_backupUrl))
                throw new InvalidOperationException("Backup URL not set.");
        }

        /// <summary>
        /// This operation returns international phone exchange information for a given phone number, including carrier,
        /// line type, formatted numbers, and location details.
        /// </summary>
        /// <param name="PhoneNumber">The phone number to validate (e.g., "+12025550123").</param>
        /// <param name="CountryCode">1-3 digit country calling code (e.g., "1"). Optional.</param>
        /// <param name="Country">ISO2, ISO3, or country name (e.g., "US"). Optional.</param>
        /// <param name="IPAddress">IPv4 address. Optional.</param>
        /// <param name="CallerCountry">ISO2 or ISO3 code representing the caller's country. Optional.</param>
        /// <param name="Extras">Comma-separated list of possible options. Optional.</param>
        /// <param name="LicenseKey">The license key to authenticate the API request.</param>
        public async Task<InternationalExchangeInfoResponse> GetInternationalExchangeInfo(string PhoneNumber, string Country, string LicenseKey)
        {
            PE2SoapClient clientPrimary = null;
            PE2SoapClient clientBackup = null;

            try
            {
                // Attempt Primary
                clientPrimary = new PE2SoapClient();
                clientPrimary.Endpoint.Address = new System.ServiceModel.EndpointAddress(_primaryUrl);
                clientPrimary.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                // Map input parameters to the simplified GetInternationalExchangeInfoAsync call
                InternationalExchangeInfoResponse response = await clientPrimary.GetInternationalExchangeInfoAsync(PhoneNumber, Country, LicenseKey).ConfigureAwait(false);

                if (_isLive && !IsValid(response))
                {
                    throw new InvalidOperationException("Primary endpoint returned null or a fatal TypeCode=3 error for GetInternationalExchangeInfo");
                }
                return response;
            }
            catch (Exception primaryEx)
            {
                try
                {
                    clientBackup = new PE2SoapClient();
                    clientBackup.Endpoint.Address = new System.ServiceModel.EndpointAddress(_backupUrl);
                    clientBackup.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                    return await clientBackup.GetInternationalExchangeInfoAsync(PhoneNumber, Country, LicenseKey).ConfigureAwait(false);
                }
                catch (Exception backupEx)
                {
                    throw new InvalidOperationException(
                        $"Both primary and backup endpoints failed.\n" +
                        $"Primary error: {primaryEx.Message}\n" +
                        $"Backup error: {backupEx.Message}");
                }
                finally
                {
                    clientBackup?.Close();
                }
            }
            finally
            {
                clientPrimary?.Close();
            }
        }

        private static bool IsValid(InternationalExchangeInfoResponse response) => response?.Error == null || response.Error.TypeCode != "3";
    }
}