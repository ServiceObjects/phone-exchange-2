export class ExchangeInfo {
    constructor(data = {}) {
        this.PhoneNumber = data.PhoneNumber;
        this.Name = data.Name;
        this.City = data.City;
        this.State = data.State;
        this.Country = data.Country;
        this.LineType = data.LineType;
        this.TimeZone = data.TimeZone;
        this.Latitude = data.Latitude;
        this.Longitude = data.Longitude;
        this.SMSAddress = data.SMSAddress;
        this.MMSAddress = data.MMSAddress;
        this.PortedInfo = data.PortedInfo;
        this.NoteCodes = data.NoteCodes;
        this.NoteDescriptions = data.NoteDescriptions;
    }

    toString() {
        return `ExchangeInfo: PhoneNumber = ${this.PhoneNumber}, Name = ${this.Name}, City = ${this.City}, State = ${this.State}, Country = ${this.Country}, LineType = ${this.LineType}, TimeZone = ${this.TimeZone}, Latitude = ${this.Latitude}, Longitude = ${this.Longitude}, SMSAddress = ${this.SMSAddress}, MMSAddress = ${this.MMSAddress}, PortedInfo = ${this.PortedInfo}, NoteCodes = ${this.NoteCodes}, NoteDescriptions = ${this.NoteDescriptions}`;
    }
}

/**
 * Ported information for a phone number.
 */
export class PortedInfo {
    constructor(data = {}) {
        this.OriginalName = data.OriginalName;
        this.OriginalLineType = data.OriginalLineType;
        this.PortedDate = data.PortedDate;
        this.LATA = data.LATA;
    }

    toString() {
        return `PortedInfo: OriginalName = ${this.OriginalName}, OriginalLineType = ${this.OriginalLineType}, PortedDate = ${this.PortedDate}, LATA = ${this.LATA}`;
    }
}

/**
 * International phone exchange information for a validated phone number.
 */
export class InternationalExchangeInfo {
    constructor(data = {}) {
        this.PhoneNumberIn = data.NumberIn;
        this.CountryCode = data.CountryCode;
        this.FormatNational = data.FormatNational;
        this.Extension = data.Extension;
        this.Locality = data.Locality;
        this.LocalityMatchLevel = data.LocalityMatchLevel;
        this.TimeZone = data.TimeZone;
        this.Latitude = data.Latitude;
        this.Longitude = data.Longitude;
        this.Country = data.Country;
        this.CountryISO2 = data.CountryISO2;
        this.CountryISO3 = data.CountryISO3;
        this.FormatInternational = data.FormatInternational;
        this.FormatE164 = data.FormatE164;
        this.Carrier = data.Carrier;
        this.LineType = data.LineType;
        this.SMSAddress = data.SMSAddress;
        this.MMSAddress = data.MMSAddress;
        this.IsValid = data.IsValid !== undefined ? data.IsValid : null;
        this.IsValidForRegion = data.IsValidForRegion !== undefined ? data.IsValidForRegion : null;
        this.NoteCodes = data.NoteCodes;
        this.NoteDescriptions = data.NoteDescriptions;
    }

    toString() {
        return `InternationalExchangeInfo: PhoneNumberIn = ${this.PhoneNumberIn}, CountryCode = ${this.CountryCode}, FormatNational = ${this.FormatNational}, Extension = ${this.Extension}, Locality = ${this.Locality}, LocalityMatchLevel = ${this.LocalityMatchLevel}, TimeZone = ${this.TimeZone}, Latitude = ${this.Latitude}, Longitude = ${this.Longitude}, Country = ${this.Country}, CountryISO2 = ${this.CountryISO2}, CountryISO3 = ${this.CountryISO3}, FormatInternational = ${this.FormatInternational}, FormatE164 = ${this.FormatE164}, Carrier = ${this.Carrier}, LineType = ${this.LineType}, SMSAddress = ${this.SMSAddress}, MMSAddress = ${this.MMSAddress}, IsValid = ${this.IsValid}, IsValidForRegion = ${this.IsValidForRegion}, NoteCodes = ${this.NoteCodes}, NoteDescriptions = ${this.NoteDescriptions}`;
    }
}

/**
 * Error object for PE2 API responses.
 */
export class Error {
    constructor(data = {}) {
        this.Desc = data.Desc;
        this.TypeCode = data.TypeCode;
        this.DescCode = data.DescCode;
        this.Type = data.Type;
    }

    toString() {
        return `Error: Desc = ${this.Desc}, TypeCode = ${this.TypeCode}, DescCode = ${this.DescCode}, Type= ${this.Type}}`;
    }
}

/**
 * Response from PE2 GetExchangeInfo and GetInternationalExchangeInfo APIs, containing phone exchange information.
 */
export class PE2Response {
    constructor(data = {}) {
        this.ExchangeInfo = Array.isArray(data.ExchangeInfoResults)
            ? data.ExchangeInfoResults.map(info => new ExchangeInfo(info))
            : [];
        this.ExchangeInfoResults = (data.ExchangeInfoResults || []).map(info => new ExchangeInfo(info));
        this.InternationalExchangeInfo = data.InternationalExchangeInfo ? new InternationalExchangeInfo(data.InternationalExchangeInfo) : null;
        this.Error = data.Error ? new Error(data.Error) : null;
    }

    toString() {
        const exchangeInfoString = this.ExchangeInfoResults.length
            ? this.ExchangeInfoResults.map(info => info.toString()).join('; ')
            : 'null';
        const internationalInfoString = this.InternationalExchangeInfo.length
            ? this.InternationalExchangeInfo.map(info => info.toString()).join('; ')
            : 'null';
        return `PE2Response: ExchangeInfoResults = [${exchangeInfoString}], InternationalExchangeInfo = [${internationalInfoString}], Error = ${this.Error ? this.Error.toString() : 'null'}`;
    }
}

export default PE2Response;