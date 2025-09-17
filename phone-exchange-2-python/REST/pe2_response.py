
from asyncio.windows_events import NULL
from dataclasses import dataclass
from typing import Optional, List, Type

@dataclass
class Error:
    Desc: Optional[str] = None
    TypeCode: Optional[str] = None
    DescCode: Optional[str] = None
    Type: Optional[str] = None

    def __str__(self) -> str:
        return f"Error: Desc={self.Desc}, TypeCode={self.TypeCode}, DescCode={self.DescCode}, Type={self.Type}"

@dataclass
class PortedInfo:
    OriginalName: Optional[str] = None
    OriginalLineType: Optional[str] = None
    PortedDate: Optional[str] = None
    LATA: Optional[str] = None

    def __str__(self) -> str:
        return (f"PortedInfo: OriginalName={self.OriginalName}, OriginalLineType={self.OriginalLineType}, "
                f"PortedDate={self.PortedDate}, LATA={self.LATA}")

@dataclass
class ExchangeInfo:
    PhoneNumber: Optional[str] = None
    Name: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    Country: Optional[str] = None
    LineType: Optional[str] = None
    TimeZone: Optional[str] = None
    Latitude: Optional[str] = None
    Longitude: Optional[str] = None
    SMSAddress: Optional[str] = None
    MMSAddress: Optional[str] = None
    PortedInfo: Optional['PortedInfo'] = None
    NoteCodes: Optional[str] = None
    NoteDescriptions: Optional[str] = None

    def __post_init__(self):
        if self.NoteCodes is None:
            self.NoteCodes = ""
        if self.NoteDescriptions is None:
            self.NoteDescriptions = ""

    def __str__(self) -> str:
        return (f"ExchangeInfo: PhoneNumber={self.PhoneNumber}, Name={self.Name}, City={self.City}, "
                f"State={self.State}, Country={self.Country}, LineType={self.LineType}, "
                f"TimeZone={self.TimeZone}, Latitude={self.Latitude}, Longitude={self.Longitude}, "
                f"SMSAddress={self.SMSAddress}, MMSAddress={self.MMSAddress}, "
                f"PortedInfo={self.PortedInfo}, NoteCodes=[{self.NoteCodes}], "
                f"NoteDescriptions={self.NoteDescriptions}")

@dataclass
class InternationalExchangeInfo:
    PhoneNumberIn: Optional[str] = None
    CountryCode: Optional[str] = None
    FormatNational: Optional[str] = None
    Extension: Optional[str] = None
    Locality: Optional[str] = None
    LocalityMatchLevel: Optional[str] = None
    TimeZone: Optional[str] = None
    Latitude: Optional[str] = None
    Longitude: Optional[str] = None
    Country: Optional[str] = None
    CountryISO2: Optional[str] = None
    CountryISO3: Optional[str] = None
    FormatInternational: Optional[str] = None
    FormatE164: Optional[str] = None
    Carrier: Optional[str] = None
    LineType: Optional[str] = None
    SMSAddress: Optional[str] = None
    MMSAddress: Optional[str] = None
    IsValid: bool = False
    IsValidForRegion: bool = False
    NoteCodes: Optional[str] = None
    NoteDescriptions: Optional[str] = None

    def __post_init__(self):
        if self.NoteCodes is None:
            self.NoteCodes = ""
        if self.NoteDescriptions is None:
            self.NoteDescriptions = ""

    def __str__(self) -> str:
        return (f"InternationalExchangeInfo: PhoneNumberIn={self.PhoneNumberIn}, CountryCode={self.CountryCode}, "
                f"FormatNational={self.FormatNational}, Extension={self.Extension}, Locality={self.Locality}, "
                f"LocalityMatchLevel={self.LocalityMatchLevel}, TimeZone={self.TimeZone}, "
                f"Latitude={self.Latitude}, Longitude={self.Longitude}, Country={self.Country}, "
                f"CountryISO2={self.CountryISO2}, CountryISO3={self.CountryISO3}, "
                f"FormatInternational={self.FormatInternational}, FormatE164={self.FormatE164}, "
                f"Carrier={self.Carrier}, LineType={self.LineType}, SMSAddress={self.SMSAddress}, "
                f"MMSAddress={self.MMSAddress}, IsValid={self.IsValid}, IsValidForRegion={self.IsValidForRegion}, "
                f"NoteCodes={self.NoteCodes}, NoteDescriptions={self.NoteDescriptions}")

@dataclass
class PE2Response:
    ExchangeInfoResults: Optional[List['ExchangeInfo']] = None
    InternationalExchangeInfo: Optional['InternationalExchangeInfo'] = None
    Error: Optional['Error'] = None

    def __post_init__(self):
        if self.ExchangeInfoResults is None:
            self.ExchangeInfoResults = []

    def __str__(self) -> str:
        exchange_info_str = '\n'.join(str(r) for r in self.ExchangeInfoResults) if self.ExchangeInfoResults else 'None'
        error_str = str(self.Error) if self.Error else 'None'
        return (f"PE2Response: ExchangeInfoResults=[\n{exchange_info_str}\n], "
                f"InternationalExchangeInfo=\n{self.InternationalExchangeInfo}\n, Error={error_str}")