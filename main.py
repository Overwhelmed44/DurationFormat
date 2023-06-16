class TimeFormat:
    """
    Language: Russian
    I hope it works correctly
    """

    def __init__(self, seconds: int):
        total = 0

        self.int_years: int = seconds // 31536000  # 1 year = 365 days
        total += self.int_years * 31536000
        self.int_weeks: int = (seconds - total) // 604800
        total += self.int_weeks * 604800
        self.int_days: int = (seconds - total) // 86400
        total += self.int_days * 86400
        self.int_hours: int = (seconds - total) // 3600
        total += self.int_hours * 3600
        self.int_minutes: int = (seconds - total) // 60
        total += self.int_minutes * 60
        self.int_seconds: int = seconds - total

        iterator = self.__convert()

        self.years: str = next(iterator)
        self.weeks: str = next(iterator)
        self.days: str = next(iterator)
        self.hours: str = next(iterator)
        self.minutes: str = next(iterator)
        self.seconds: str = next(iterator)
        self.tuple_of_strings: tuple = tuple(filter(
            lambda arg: bool(arg),
            (self.years, self.weeks, self.days, self.hours, self.minutes, self.seconds)
        ))

    def __convert(self):
        for arr in (
            (self.int_years, 'лет', 'год', 'года'),
            (self.int_weeks, 'недель', 'неделя', 'недели'),
            (self.int_days, 'дней', 'день', 'дня'),
            (self.int_hours, 'часов', 'час', 'часа'),
            (self.int_minutes, 'минут', 'минута', 'минуты'),
            (self.int_seconds, 'секунд', 'секунда', 'секунды')
        ):
            if not (a := arr[0]):
                yield ''
            else:
                s = str(a)
                last = s[-1]
                result = s + ' '
                if (len(s) >= 2 and s[-2] == '1') or last in '567890':
                    yield result + arr[1]
                elif last == '1':
                    yield result + arr[2]
                else:
                    yield result + arr[3]

    def __iter__(self):
        for string in self.tuple_of_strings:
            yield string

    def __str__(self):
        return ', '.join(self.tuple_of_strings[:-1]) + f' и {self.tuple_of_strings[-1]}'
