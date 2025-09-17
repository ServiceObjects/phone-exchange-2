from pe2_response import PE2Response, ExchangeInfo, InternationalExchangeInfo, PortedInfo, Error
import requests

# Endpoint URLs for ServiceObjects Phone Exchange (PE2) API
primary_url = "https://trial.serviceobjects.com/pe2/web.svc/json/GetInternationalExchangeInfo?"
backup_url = "https://swsbackup.serviceobjects.com/pe2/web.svc/json/GetInternationalExchangeInfo?"
trial_url = "https://trial.serviceobjects.com/pe2/web.svc/json/GetInternationalExchangeInfo?"

def get_international_exchange_info(
    phone_number: str,
    country: str = None,
    license_key: str = None,
    is_live: bool = True
) -> PE2Response:
    """
    Call ServiceObjects Phone Exchange (PE2) API's GetInternationalExchangeInfo endpoint
    to retrieve international phone exchange information for a given phone number.

    Parameters:
        phone_number: The phone number to validate, including country code if no country is provided.
        country: ISO2, ISO3, or full country name (e.g., "US", "USA", "United States"). Optional.
        license_key: Your ServiceObjects license key.
        is_live: Use live or trial servers.

    Returns:
        PE2Response: Parsed JSON response with international phone exchange results or error details.

    Raises:
        RuntimeError: If the API returns an error payload.
        requests.RequestException: On network/HTTP failures (trial mode).
    """
    params = {
        "PhoneNumber": phone_number,
        "Country": country,
        "LicenseKey": license_key,
    }
    # Select the base URL: production vs trial
    url = primary_url if is_live else trial_url

    try:
        # Attempt primary (or trial) endpoint
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # If API returned an error in JSON payload, trigger fallback
        error = data.get('Error')
        if not (error is None or error.get('TypeCode') != "3"):
            if is_live:
                # Try backup URL
                response = requests.get(backup_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()

                # If still error, propagate exception
                if 'Error' in data:
                    raise RuntimeError(f"Phone Exchange service error: {data['Error']}")
            else:
                # Trial mode error is terminal
                raise RuntimeError(f"Phone Exchange trial error: {data['Error']}")

        # Convert JSON response to PE2Response for structured access
        error = Error(**data.get("Error", {})) if data.get("Error") else None

        if "InternationalExchangeInfo" in data:
            exchange_info_data = data["InternationalExchangeInfo"]
            if isinstance(exchange_info_data, dict):
                international_exchange_info = InternationalExchangeInfo(
                    PhoneNumberIn=exchange_info_data.get("NumberIn"),
                    CountryCode=exchange_info_data.get("CountryCode"),
                    FormatNational=exchange_info_data.get("FormatNational"),
                    Extension=exchange_info_data.get("Extension"),
                    Locality=exchange_info_data.get("Locality"),
                    LocalityMatchLevel=exchange_info_data.get("LocalityMatchLevel"),
                    TimeZone=exchange_info_data.get("TimeZone"),
                    Latitude=exchange_info_data.get("Latitude"),
                    Longitude=exchange_info_data.get("Longitude"),
                    Country=exchange_info_data.get("Country"),
                    CountryISO2=exchange_info_data.get("CountryISO2"),
                    CountryISO3=exchange_info_data.get("CountryISO3"),
                    FormatInternational=exchange_info_data.get("FormatInternational"),
                    FormatE164=exchange_info_data.get("FormatE164"),
                    Carrier=exchange_info_data.get("Carrier"),
                    LineType=exchange_info_data.get("LineType"),
                    SMSAddress=exchange_info_data.get("SMSAddress"),
                    MMSAddress=exchange_info_data.get("MMSAddress"),
                    IsValid=exchange_info_data.get("IsValid"),
                    IsValidForRegion=exchange_info_data.get("IsValidForRegion"),
                    NoteCodes=exchange_info_data.get("NoteCodes"),
                    NoteDescriptions=exchange_info_data.get("NoteDescriptions")
                )
        return PE2Response(
            InternationalExchangeInfo=international_exchange_info,
            Error=error
        )

    except requests.RequestException as req_exc:
        # Network or HTTP-level error occurred
        if is_live:
            try:
                response = requests.get(backup_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                if "Error" in data:
                    raise RuntimeError(f"Phone Exchange backup error: {data['Error']}") from req_exc

                error = Error(**data.get("Error", {})) if data.get("Error") else None
                international_exchange_info = []

                if "InternationalExchangeInfo" in data:
                    exchange_info_data = data["InternationalExchangeInfo"]
                    if isinstance(exchange_info_data, dict):
                        international_exchange_info.append(InternationalExchangeInfo(
                            PhoneNumberIn=exchange_info_data.get("NumberIn"),
                            CountryCode=exchange_info_data.get("CountryCode"),
                            FormatNational=exchange_info_data.get("FormatNational"),
                            Extension=exchange_info_data.get("Extension"),
                            Locality=exchange_info_data.get("Locality"),
                            LocalityMatchLevel=exchange_info_data.get("LocalityMatchLevel"),
                            TimeZone=exchange_info_data.get("TimeZone"),
                            Latitude=exchange_info_data.get("Latitude"),
                            Longitude=exchange_info_data.get("Longitude"),
                            Country=exchange_info_data.get("Country"),
                            CountryISO2=exchange_info_data.get("CountryISO2"),
                            CountryISO3=exchange_info_data.get("CountryISO3"),
                            FormatInternational=exchange_info_data.get("FormatInternational"),
                            FormatE164=exchange_info_data.get("FormatE164"),
                            Carrier=exchange_info_data.get("Carrier"),
                            LineType=exchange_info_data.get("LineType"),
                            SMSAddress=exchange_info_data.get("SMSAddress"),
                            MMSAddress=exchange_info_data.get("MMSAddress"),
                            IsValid=exchange_info_data.get("IsValid"),
                            IsValidForRegion=exchange_info_data.get("IsValidForRegion"),
                            NoteCodes=exchange_info_data.get("NoteCodes", []),
                            NoteDescriptions=exchange_info_data.get("NoteDescriptions", [])
                        ))
                return PE2Response(
                    InternationalExchangeInfo=international_exchange_info,
                    Error=error
                )
            except Exception as backup_exc:
                raise RuntimeError("Phone Exchange service unreachable on both endpoints") from backup_exc
        else:
            raise RuntimeError(f"Phone Exchange trial error: {str(req_exc)}") from req_exc