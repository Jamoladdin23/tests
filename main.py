def is_even(num: int) -> bool:
    return num % 2 == 0


def is_odd(num: int) -> bool:  # obratniy poryadok proverki, ne parnie li chisla
    return num % 2 != 0


def add(a: int, b: int) -> int:
    return a + b


def api_request(location):
    # pristavim wo tut really zapros na sozdanya api
    return "sunny"


def fetch_weather(location):
    weather = api_request(location)
    if weather == "sunny":
        return "it's a sunny day in {}".format(location)
    return "Weather in {}: {}".format(location, weather)
