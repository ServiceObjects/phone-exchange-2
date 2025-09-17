export class ExchangeInfo {
    constructor(data = {}) {
        this.PhoneNumber = data.PhoneNumber || null;
        this.Name = data.Name || null;
        this.City = data.City || null;
        this.State = data.State || null;
        this.Country = data.Country || null;
        this.LineType = data.LineType || null;
        this.TimeZone = data.TimeZone || null;
        this.Latitude = data.Latitude || null;
        this.Longitude = data.Longitude || null;
        this.SMSAddress = data.SMSAddress || null;
        this.MMSAddress = data.MMSAddress || null;
        this.PortedInfo = data.PortedInfo || null;
        this.NoteCodes = data.NoteCodes || null;
        this.NoteDescriptions = data.NoteDescriptions || null;
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
        this.OriginalName = data.OriginalName || null;
        this.OriginalLineType = data.OriginalLineType || null;
        this.PortedDate = data.PortedDate || null;
        this.LATA = data.LATA || null;
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
        this.PhoneNumberIn = data.NumberIn || null;
        this.CountryCode = data.CountryCode || null;
        this.FormatNational = data.FormatNational || null;
        this.Extension = data.Extension || null;
        this.Locality = data.Locality || null;
        this.LocalityMatchLevel = data.LocalityMatchLevel || null;
        this.TimeZone = data.TimeZone || null;
        this.Latitude = data.Latitude || null;
        this.Longitude = data.Longitude || null;
        this.Country = data.Country || null;
        this.CountryISO2 = data.CountryISO2 || null;
        this.CountryISO3 = data.CountryISO3 || null;
        this.FormatInternational = data.FormatInternational || null;
        this.FormatE164 = data.FormatE164 || null;
        this.Carrier = data.Carrier || null;
        this.LineType = data.LineType || null;
        this.SMSAddress = data.SMSAddress || null;
        this.MMSAddress = data.MMSAddress || null;
        this.IsValid = data.IsValid !== undefined ? data.IsValid : null;
        this.IsValidForRegion = data.IsValidForRegion !== undefined ? data.IsValidForRegion : null;
        this.NoteCodes = data.NoteCodes || null;
        this.NoteDescriptions = data.NoteDescriptions || null;
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
        this.Desc = data.Desc || null;
        this.TypeCode = data.TypeCode || null;
        this.DescCode = data.DescCode || null;
        this.Type = data.Type || null;
    }

    toString() {
        return `Error: Desc = ${this.Desc}, TypeCode = ${this.TypeCode}, DescCode = ${this.DescCode}, Type = ${this.Type}`;
    }
}

/**
 * Response from PE2 GetExchangeInfo and GetInternationalExchangeInfo APIs, containing phone exchange information.
 */
export class PE2Response {
    constructor(data = {}) {
        const exchangeInfo = Array.isArray(data?.ExchangeInfoResults?.ExchangeInfo)
            ? data.ExchangeInfoResults.ExchangeInfo
            : [];

        this.ExchangeInfo = exchangeInfo.map(info => new ExchangeInfo(info));
        this.ExchangeInfoResults = this.ExchangeInfo;

        this.InternationalExchangeInfo = data.InternationalExchangeInfo

        this.Error = data?.Error ? new Error(data.Error) : null;
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