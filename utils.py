from datetime import datetime

## ========================= TDD ============================

def formatDate(date: datetime) -> str:
    """
    Take a Date object and transform it to the format yyyy-MM-dd and return
    :param date: Object Date
    :returns: String with the format yyyy-MM-dd, ex : "2024-08-31"
    """
    return None

def parseDate(date_string: str) -> datetime:
    """
    Take a string as input in the format yyyy-MM-dd to make it an object Date.
    :param date_string: String, ex : "2024-08-31"
    :returns: object Date
    """
    return None

def formatDateWithPattern(date: datetime, pattern: str) -> str:
    """
    Take a Date object and transform it to the format given in input if it is valid
    :param date: Object Date
    :param pattern: The pattern of the desired date, ex : yyyy-MM-dd or dd/MM/YYYY
    :returns: String formatted with the pattern in input ex : "31/08/2024"
    """
    return None

## ========================= Test by description ============================

def formatDateTime(date: datetime) -> str:
    """
    Take a Date object and transform it to the format yyyy-MM-ddThh:mm:ss and return
    a string
    :param date: Object Date
    :returns: String with the format yyyy-MM-ddThh:mm:ss, ex : "2024-08-31T08:46:00"
    """
    return None

def parseDateTime(date_string: str) -> datetime:
    """
    Take a string as input in the format yyyy-MM-ddThh:mm:ss to make it an object Date.
    :param date_string: String, ex : "2024-08-31T08:46:00"
    :returns: object Date
    """
    return None

## ========================= Test by code ============================

def formatDateTimeWithPattern(date_time: datetime, pattern: str) -> str:
    """
    Take a Date object and transform it to the format given in input if it is valid
    :param date_time: Object Date
    :param pattern: The pattern of the desired date, ex : yyyy-MM-dd or dd/MM/YYYY
    :returns: String formatted with the pattern in input ex : "31/08/2024"
    """
    if not date_time or not isinstance(date_time, datetime):
        return None

    year = date_time.year
    month = f'{date_time.month:02}'
    day = f'{date_time.day:02}'
    hours = f'{date_time.hour:02}'
    minutes = f'{date_time.minute:02}'
    seconds = f'{date_time.second:02}'

    formatted_date = pattern.replace('yyyy', str(year)) \
                            .replace('MM', month) \
                            .replace('dd', day) \
                            .replace('hh', hours) \
                            .replace('mm', minutes) \
                            .replace('ss', seconds)

    return formatted_date