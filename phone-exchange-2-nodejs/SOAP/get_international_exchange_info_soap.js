import { soap } from 'strong-soap'
import { PE2Response } from './pe2_response.js';
/**
 * A class that provides functionality to call the ServiceObjects Phone Exchange (PE2) SOAP service's GetInternationalExchangeInfo endpoint,
 * retrieving international phone exchange information (e.g., country code, line type, locality) for a given phone number with fallback to a backup endpoint for reliability in live mode.
 */
class GetInternationalExchangeInfoSoap {
    /**
     * Initializes a new instance of the GetInternationalExchangeInfoSoap class with the provided input parameters,
     * setting up primary and backup WSDL URLs based on the live/trial mode.
     * @param {string} PhoneNumber - The phone number to validate (e.g., "+12025550123").
     * @param {string} Country - The country in ISO2, ISO3, or full name format (e.g., "US").
     * @param {string} LicenseKey - Your license key to use the service.
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     */
    constructor(PhoneNumber, Country, LicenseKey, isLive, timeoutSeconds) {
        if (!LicenseKey) {
            throw new Error('LicenseKey is required.');
        }

        this.args = {
            PhoneNumber,
            Country,
            LicenseKey
        };

        this.isLive = isLive !== undefined ? isLive : true;
        this.timeoutSeconds = timeoutSeconds !== undefined ? timeoutSeconds : 15;

        this.LiveBaseUrl = 'https://sws.serviceobjects.com/PE2/soap.svc?wsdl';
        this.BackupBaseUrl = 'https://swsbackup.serviceobjects.com/PE2/soap.svc?wsdl';
        this.TrialBaseUrl = 'https://trial.serviceobjects.com/PE2/soap.svc?wsdl';

        this._primaryWsdl = this.isLive ? this.LiveBaseUrl : this.TrialBaseUrl;
        this._backupWsdl = this.isLive ? this.BackupBaseUrl : this.TrialBaseUrl;
    }

    /**
     * Asynchronously calls the GetInternationalExchangeInfo SOAP endpoint, attempting the primary endpoint
     * first and falling back to the backup if the response is invalid (Error.TypeCode == '3') in live mode
     * or if the primary call fails.
     * @returns {Promise} A promise that resolves to a PE2Response object containing international exchange info or an error.
     */
    async invokeAsync() {
        try {
            const primaryResult = await this._callSoap(this._primaryWsdl, this.args);

            if (this.isLive && !this._isValid(primaryResult)) {
                console.warn("Primary returned Error.TypeCode == '3', falling back to backup...");
                const backupResult = await this._callSoap(this._backupWsdl, this.args);
                return new PE2Response(backupResult);
            }

            return new PE2Response(primaryResult);
        } catch (primaryErr) {
            try {
                const backupResult = await this._callSoap(this._backupWsdl, this.args);
                return new PE2Response(backupResult);
            } catch (backupErr) {
                throw new Error(`Both primary and backup calls failed:\nPrimary: ${primaryErr.message}\nBackup: ${backupErr.message}`);
            }
        }
    }

    /**
     * Performs a SOAP service call to the specified WSDL URL with the given arguments,
     * creating a client and processing the response into an object.
     * @param {string} wsdlUrl - The WSDL URL of the SOAP service endpoint (primary or backup).
     * @param {Object} args - The arguments to pass to the GetInternationalExchangeInfo method.
     * @returns {Promise} A promise that resolves to an object containing the SOAP response data.
     */
    _callSoap(wsdlUrl, args) {
        return new Promise((resolve, reject) => {
            soap.createClient(wsdlUrl, { timeout: this.timeoutSeconds * 1000 }, (err, client) => {
                if (err) return reject(err);

                client.GetInternationalExchangeInfo(args, (err, result) => {
                    const response = result?.GetInternationalExchangeInfoResult;
                    try {
                        if (!response) {
                            return reject(new Error('SOAP response is empty or undefined.'));
                        }
                        resolve(response);
                    } catch (parseErr) {
                        reject(new Error(`Failed to parse SOAP response: ${parseErr.message}`));
                    }
                });
            });
        });
    }

    /**
     * Checks if a SOAP response is valid by verifying that it exists and either has no Error object
     * or the Error.TypeCode is not equal to '3'.
     * @param {Object} response - The response object to validate.
     * @returns {boolean} True if the response is valid, false otherwise.
     */
    _isValid(response) {
        return response && (!response.Error || response.Error.TypeCode !== '3');
    }
}

export { GetInternationalExchangeInfoSoap };