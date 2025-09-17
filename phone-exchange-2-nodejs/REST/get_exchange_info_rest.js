import axios from 'axios';
import querystring from 'querystring';
import {PE2Response} from './pe2_response.js';

/**
 * @constant
 * @type {string}
 * @description The base URL for the live ServiceObjects Phone Exchange (PE2) API service.
 */
const LiveBaseUrl = 'https://sws.serviceobjects.com/pe2/web.svc/json/';

/**
 * @constant
 * @type {string}
 * @description The base URL for the backup ServiceObjects Phone Exchange (PE2) API service.
 */
const BackupBaseUrl = 'https://swsbackup.serviceobjects.com/pe2/web.svc/json/';

/**
 * @constant
 * @type {string}
 * @description The base URL for the trial ServiceObjects Phone Exchange (PE2) API service.
 */
const TrialBaseUrl = 'https://trial.serviceobjects.com/pe2/web.svc/json/';

/**
 * <summary>
 * Checks if a response from the API is valid by verifying that it either has no Error object
 * or the Error.TypeCode is not equal to '3'.
 * </summary>
 * <param name="response" type="Object">The API response object to validate.</param>
 * <returns type="boolean">True if the response is valid, false otherwise.</returns>
 */
const isValid = (response) => !response?.Error || response.Error.TypeCode !== '3';

/**
 * <summary>
 * Constructs a full URL for the GetExchangeInfo API endpoint by combining the base URL
 * with query parameters derived from the input parameters.
 * </summary>
 * <param name="params" type="Object">An object containing all the input parameters.</param>
 * <param name="baseUrl" type="string">The base URL for the API service (live, backup, or trial).</param>
 * <returns type="string">The constructed URL with query parameters.</returns>
 */
const buildUrl = (params, baseUrl) =>
    `${baseUrl}GetExchangeInfo?${querystring.stringify(params)}`;

/**
 * <summary>
 * Performs an HTTP GET request to the specified URL with a given timeout.
 * </summary>
 * <param name="url" type="string">The URL to send the GET request to.</param>
 * <param name="timeoutSeconds" type="number">The timeout duration in seconds for the request.</param>
 * <returns type="Promise<PE2Response>">A promise that resolves to a PE2Response object containing the API response data.</returns>
 * <exception cref="Error">Thrown if the HTTP request fails, with a message detailing the error.</exception>
 */
const httpGet = async (url, timeoutSeconds) => {
    try {
        const response = await axios.get(url, { timeout: timeoutSeconds * 1000 });
        return new PE2Response(response.data);
    } catch (error) {
        throw new Error(`HTTP request failed: ${error.message}`);
    }
};

/**
 * <summary>
 * Provides functionality to call the ServiceObjects Phone Exchange (PE2) API's GetExchangeInfo endpoint,
 * retrieving phone exchange information (e.g., carrier, line type, ported status) for a given US/Canada phone number
 * with fallback to a backup endpoint for reliability in live mode.
 * </summary>
 */
const GetExchangeInfoClient = {
    /**
     * <summary>
     * Asynchronously invokes the GetExchangeInfo API endpoint, attempting the primary endpoint
     * first and falling back to the backup if the response is invalid (Error.TypeCode == '3') in live mode.
     * </summary>
     * @param {string} PhoneNumber - The phone number to validate (e.g., "1234567890").
     * @param {string} CountryCode - 1-3 digit country calling code (e.g., "1"). Optional.
     * @param {string} Country - ISO2, ISO3, or country name (e.g., "US"). Optional.
     * @param {string} IPAddress - IPv4 address. Optional.
     * @param {string} CallerCountry - ISO2 or ISO3 code representing the caller's country. Optional.
     * @param {string} Extras - Comma-separated list of possible options. Optional.
     * @param {string} Token - Your token to use the service. Sign up for a free token at.
     * @param {string} LicenseKey - Your license key to use the service.
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     * @returns {Promise<PE2Response>} - A promise that resolves to a PE2Response object.
     */
    async invokeAsync(PhoneNumber, CountryCode, Country, IPAddress, CallerCountry, Extras,Token, LicenseKey, isLive = true, timeoutSeconds = 15) {
        const params = {
            PhoneNumber,
            CountryCode,
            Country,
            IPAddress,
            CallerCountry,
            Extras,
            Token,
            LicenseKey
        };

        const url = buildUrl(params, isLive ? LiveBaseUrl : TrialBaseUrl);
        let response = await httpGet(url, timeoutSeconds);

        if (isLive && !isValid(response)) {
            const fallbackUrl = buildUrl(params, BackupBaseUrl);
            const fallbackResponse = await httpGet(fallbackUrl, timeoutSeconds);
            return fallbackResponse;
        }
        return response;
    },

    /**
     * <summary>
     * Synchronously invokes the GetExchangeInfo API endpoint by wrapping the async call
     * and awaiting its result immediately.
     * </summary>
     * @param {string} PhoneNumber - The phone number to validate (e.g., "1234567890").
     * @param {string} CountryCode - 1-3 digit country calling code (e.g., "1"). Optional.
     * @param {string} Country - ISO2, ISO3, or country name (e.g., "US"). Optional.
     * @param {string} IPAddress - IPv4 address. Optional.
     * @param {string} CallerCountry - ISO2 or ISO3 code representing the caller's country. Optional.
     * @param {string} Extras - Comma-separated list of possible options. Optional.
     * @param {string} Token - Your token to use the service. Sign up for a free token at.
     * @param {string} LicenseKey - Your license key to use the service.
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     * @returns {PE2Response} - A PE2Response object with phone exchange details or an error.
     */
    invoke(PhoneNumber, CountryCode, Country, IPAddress, CallerCountry, Extras,Token, LicenseKey, isLive = true, timeoutSeconds = 15) {
        return (async () => await this.invokeAsync(
            PhoneNumber, CountryCode, Country, IPAddress, CallerCountry, Extras, Token, LicenseKey, isLive, timeoutSeconds
        ))();
    }
};

export { GetExchangeInfoClient, PE2Response };