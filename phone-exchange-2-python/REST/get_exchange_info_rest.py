from pe2_response import PE2Response, ExchangeInfo, InternationalExchangeInfo, PortedInfo, Error
import requests

# Endpoint URLs for ServiceObjects Phone Exchange (PE2) API
primary_url = "https://sws.serviceobjects.com/pe2/web.svc/json/GetExchangeInfo?"
backup_url = "https://swsbackup.serviceobjects.com/pe2/web.svc/json/GetExchangeInfo?"
trial_url = "https://trial.serviceobjects.com/pe2/web.svc/json/GetExchangeInfo?"

def get_exchange_info(
    phone_number: str,
    license_key: str = None,
    is_live: bool = True
) -> PE2Response:
    """
    Call ServiceObjects Phone Exchange (PE2) API's GetExchangeInfo endpoint
    to retrieve phone exchange information for a given US/Canada phone number.

    Parameters:
        phone_number: The phone number to validate (e.g., "8051234567").
        license_key: Your ServiceObjects license key.
        is_live: Use live or trial servers.

    Returns:
        PE2Response: Parsed JSON response with phone exchange results or error details.

    Raises:
        RuntimeError: If the API returns an error payload.
        requests.RequestException: On network/HTTP failures (trial mode).
    """
    params = {
        "PhoneNumber": phone_number,
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
        exchange_info_results = []
        if "ExchangeInfoResults" in data:
            for ei in data.get("ExchangeInfoResults", []):
                if isinstance(ei, dict):
                    ported_info_list = []
                    if "PortedInfo" in ei and ei.get("PortedInfo"):
                        for pi in ei.get("PortedInfo", []):
                            if isinstance(pi, dict):
                                ported_info_list.append(PortedInfo(
                                    OriginalName=pi.get("OriginalName"),
                                    OriginalLineType=pi.get("OriginalLineType"),
                                    PortedDate=pi.get("PortedDate"),
                                    LATA=pi.get("LATA")
                                ))
                    exchange_info_results.append(ExchangeInfo(
                        PhoneNumber=ei.get("PhoneNumber"),
                        Name=ei.get("Name"),
                        City=ei.get("City"),
                        State=ei.get("State"),
                        Country=ei.get("Country"),
                        LineType=ei.get("LineType"),
                        TimeZone=ei.get("TimeZone"),
                        Latitude=ei.get("Latitude"),
                        Longitude=ei.get("Longitude"),
                        SMSAddress=ei.get("SMSAddress"),
                        MMSAddress=ei.get("MMSAddress"),
                        PortedInfo=ported_info_list,
                        NoteCodes=ei.get("NoteCodes", []),
                        NoteDescriptions=ei.get("NoteDescriptions", [])
                    ))

        return PE2Response(
            ExchangeInfoResults=exchange_info_results,
            Error=error
        )

    except requests.RequestException as req_exc:
        # Network or HTTP-level error occurred
        if is_live:
            try:
                # Fallback to backup URL
                response = requests.get(backup_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                if "Error" in data:
                    raise RuntimeError(f"Phone Exchange backup error: {data['Error']}") from req_exc

                error = Error(**data.get("Error", {})) if data.get("Error") else None
                exchange_info_results = []
                if "ExchangeInfoResults" in data:
                    for ei in data.get("ExchangeInfoResults", []):
                        if isinstance(ei, dict):
                            ported_info_list = []
                            if "PortedInfo" in ei and ei.get("PortedInfo"):
                                for pi in ei.get("PortedInfo", []):
                                    if isinstance(pi, dict):
                                        ported_info_list.append(PortedInfo(
                                            OriginalName=pi.get("OriginalName"),
                                            OriginalLineType=pi.get("OriginalLineType"),
                                            PortedDate=pi.get("PortedDate"),
                                            LATA=pi.get("LATA")
                                        ))
                            exchange_info_results.append(ExchangeInfo(
                                PhoneNumber=ei.get("PhoneNumber"),
                                Name=ei.get("Name"),
                                City=ei.get("City"),
                                State=ei.get("State"),
                                Country=ei.get("Country"),
                                LineType=ei.get("LineType"),
                                TimeZone=ei.get("TimeZone"),
                                Latitude=ei.get("Latitude"),
                                Longitude=ei.get("Longitude"),
                                SMSAddress=ei.get("SMSAddress"),
                                MMSAddress=ei.get("MMSAddress"),
                                PortedInfo=ported_info_list,
                                NoteCodes=ei.get("NoteCodes", []),
                                NoteDescriptions=ei.get("NoteDescriptions", [])
                            ))
                return PE2Response(
                    ExchangeInfoResults=exchange_info_results,
                    Error=error
                )
            except Exception as backup_exc:
                raise RuntimeError("Phone Exchange service unreachable on both endpoints") from backup_exc
        else:
            raise RuntimeError(f"Phone Exchange trial error: {str(req_exc)}") from req_exc