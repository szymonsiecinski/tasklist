# code inspired by https://gist.github.com/n0m4dz/ee41d4ca84e2630e70c6

from datetime import timedelta

DAY = {
    'singular': 'dzień',
    'plural1': 'dni',
    'plural2': 'dni'
}

MONTH = {
    'singular': 'miesiąc',
    'plural1': 'miesiące',
    'plural2': 'miesięcy'
}

YEAR = {
    'singular': 'rok',
    'plural1': 'lata',
    'plural2': 'lat'
}

HOUR = {
    'singular': 'godzina',
    'plural1': 'godziny',
    'plural2': 'godzin'
}

MINUTE = {
    'singular': 'minuta',
    'plural1': 'minuty',
    'plural2': 'minut'
}

SECOND = {
    'singular': 'sekunda',
    'plural1': 'sekundy',
    'plural2': 'sekund'
}


def _pluralize(quantity, dictionary):

    remainder = quantity % 10

    if isinstance(dictionary, dict):
        if 1 < remainder < 5:
            return dictionary['plural1']
        elif quantity == 1:
            return dictionary['singular']
        else:
            return dictionary['plural2']
    else:
        raise TypeError('Nie podano słownika')


def localize(timespan):
    if isinstance(timespan, timedelta):
        days = int(timespan.days % 365) % 30
        months = int((timespan.days % 365) / 30)
        years = int(timespan.days / 365)
        hours = int(timespan.seconds / 3600)
        minutes = int(timespan.seconds / 60) % 60
        seconds = timespan.seconds % 60

        days_str = _pluralize(days, DAY)
        months_str = _pluralize(months, MONTH)
        years_str = _pluralize(years, YEAR)
        hours_str = _pluralize(hours, HOUR)
        minutes_str = _pluralize(minutes, MINUTE)
        seconds_str = _pluralize(seconds, SECOND)

        return_string = ""

        if years != 0:
            return_string += "{} {}".format(years, years_str)
        if months != 0:
            return_string += " {} {}".format(months, months_str)
        if days != 0:
            return_string += " {} {}".format(days, days_str)
        if hours != 0:
            return_string += " {} {}".format(hours, hours_str)
        if minutes != 0:
            return_string += " {} {}".format(minutes, minutes_str)
        if seconds != 0:
            return_string += " {} {}".format(seconds, seconds_str)

        return return_string
    else:
        raise TypeError('Niepoprawny typ danych wejściowych')
