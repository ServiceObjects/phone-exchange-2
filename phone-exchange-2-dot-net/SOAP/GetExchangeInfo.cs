using PE2Reference;

namespace phone_exchange_2_dot_net.SOAP
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects Phone Exchange (PE2) SOAP service's GetExchangeInfo operation,
    /// retrieving phone exchange information (e.g., carrier, line type, ported status) for a given phone number
    /// with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public class GetExchangeInfoValidation
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
        public GetExchangeInfoValidation(bool isLive)
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
        /// This operation returns phone exchange information for a given phone number, including carrier,
        /// line type, ported status, SMS/MMS addresses, and location details.
        /// </summary>
        /// <param name="PhoneNumber">The phone number to validate (e.g., "1234567890").</param>
        /// <param name="LicenseKey">The license key to authenticate the API request.</param>
        public async Task<ExchangeInfoResponse> GetExchangeInfo(string PhoneNumber, string LicenseKey)
        {
            PE2SoapClient clientPrimary = null;
            PE2SoapClient clientBackup = null;

            try
            {
                // Attempt Primary
                clientPrimary = new PE2SoapClient();
                clientPrimary.Endpoint.Address = new System.ServiceModel.EndpointAddress(_primaryUrl);
                clientPrimary.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                ExchangeInfoResponse response = await clientPrimary.GetExchangeInfoAsync(PhoneNumber, LicenseKey).ConfigureAwait(false);

                if (_isLive && !IsValid(response))
                {
                    throw new InvalidOperationException("Primary endpoint returned null or a fatal TypeCode=3 error for GetExchangeInfo");
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

                    return await clientBackup.GetExchangeInfoAsync(PhoneNumber, LicenseKey).ConfigureAwait(false);
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

        private static bool IsValid(ExchangeInfoResponse response) => response?.Error == null || response.Error.TypeCode != "3";
    }
}