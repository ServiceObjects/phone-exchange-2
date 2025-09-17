from suds.client import Client
from suds import WebFault
from suds.sudsobject import Object


class GetExchangeInfoSoap:
    def __init__(self, license_key: str, is_live: bool = True, timeout_ms: int = 15000):
        """
        Initialize the GetExchangeInfoSoap client for ServiceObjects Phone Exchange (PE2) API.

        Parameters:
            license_key: ServiceObjects PE2 license key.
            is_live: Whether to use live or trial endpoints.
            timeout_ms: SOAP call timeout in milliseconds.
        """
        self.is_live = is_live
        self.timeout = timeout_ms / 1000.0
        self.license_key = license_key

        # WSDL URLs
        self._primary_wsdl = (
            "https://sws.serviceobjects.com/pe2/soap.svc?wsdl"
            if is_live
            else "https://trial.serviceobjects.com/pe2/soap.svc?wsdl"
        )
        self._backup_wsdl = (
            "https://swsbackup.serviceobjects.com/pe2/soap.svc?wsdl"
            if is_live
            else "https://trial.serviceobjects.com/pe2/soap.svc?wsdl"
        )

    def get_exchange_info(
        self,
        phone_number: str,
    ) -> Object:
        """
        Calls the GetExchangeInfo SOAP API to retrieve phone exchange information for a US/Canada phone number.

        Parameters:
            phone_number: The phone number to validate (e.g., "8051234567").
            license_key: Your ServiceObjects license key.
            is_live: Determines whether to use the live or trial servers.
            timeout_ms: Timeout, in milliseconds, for the call to the service.

        Returns:
            suds.sudsobject.Object: SOAP response containing phone exchange details or error.
        """
        # Common kwargs for both calls
        call_kwargs = dict(
            PhoneNumber=phone_number,
            LicenseKey=self.license_key,
        )

        # Attempt primary
        try:
            client = Client(self._primary_wsdl, timeout=self.timeout)
            # Override endpoint URL if needed:
            # client.set_options(location=self._primary_wsdl.replace('?wsdl','/soap'))
            response = client.service.GetExchangeInfo(**call_kwargs)

            # If response invalid or Error.TypeCode == "3", trigger fallback
            if response is None or (
                hasattr(response, "Error")
                and response.Error
                and response.Error.TypeCode == "3"
            ):
                raise ValueError("Primary returned no result or Error.TypeCode=3")

            return response

        except (WebFault, ValueError, Exception) as primary_ex:
            # Attempt backup
            try:
                client = Client(self._backup_wsdl)
                response = client.service.GetExchangeInfo(**call_kwargs)
                if response is None:
                    raise ValueError("Backup returned no result")
                return response
            except (WebFault, Exception) as backup_ex:
                msg = (
                    "Both primary and backup endpoints failed.\n"
                    f"Primary error: {str(primary_ex)}\n"
                    f"Backup error: {str(backup_ex)}"
                )
                raise RuntimeError(msg)




