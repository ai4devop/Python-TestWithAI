from datetime import datetime

## ========================= TDD ===========================
def formatDate(date: datetime) -> str:
    """
    Prend un objet Date et le transforme au format yyyy-MM-dd et le retourne
    :param date: Objet Date
    :returns: Chaîne de caractères au format yyyy-MM-dd, ex : "2024-08-31"
    """
    return None

def parseDate(date_string: str) -> datetime:
    """
    Prend une chaîne de caractères au format yyyy-MM-dd et la transforme en objet Date.
    :param date_string: Chaîne de caractères, ex : "2024-08-31"
    :returns: Objet Date
    """
    return None

def formatDateWithPattern(date: datetime, pattern: str) -> str:
    """
    Prend un objet Date et le transforme au format donné en entrée s'il est valide
    :param date: Objet Date
    :param pattern: Le format de la date souhaitée, ex : yyyy-MM-dd ou dd/MM/YYYY
    :returns: Chaîne de caractères formatée avec le pattern en entrée, ex : "31/08/2024"
    """
    return None

## ========================= Test par description ============================

def formatDateTime(date: datetime) -> str:
    """
    Prend un objet Date et le transforme au format yyyy-MM-ddThh:mm:ss et retourne
    une chaîne de caractères
    :param date: Objet Date
    :returns: Chaîne de caractères au format yyyy-MM-ddThh:mm:ss, ex : "2024-08-31T08:46:00"
    """
    return None

def parseDateTime(date_string: str) -> datetime:
    """
    Prend une chaîne de caractères au format yyyy-MM-ddThh:mm:ss et la transforme en objet Date.
    :param date_string: Chaîne de caractères, ex : "2024-08-31T08:46:00"
    :returns: Objet Date
    """
    return None

## ========================= Test par code ============================

def formatDateTimeWithPattern(date_time: datetime, pattern: str) -> str:
    """
    Prend un objet Date et le transforme au format donné en entrée s'il est valide
    :param date_time: Objet Date
    :param pattern: Le format de la date souhaitée, ex : yyyy-MM-dd ou dd/MM/YYYY
    :returns: Chaîne de caractères formatée avec le pattern en entrée, ex : "31/08/2024"
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