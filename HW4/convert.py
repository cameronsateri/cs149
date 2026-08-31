def celsius_to_fahrenheit(x):
    f = (9.0/5.0) * x + 32
    return f


def kilometers_to_miles(x):
    m = x / 1.60934
    return m


def miles_to_kilometers(x):
    km = x * 1.60934
    return km


def meters_per_second_to_miles_per_hour(x):
    km = x / 1000.0
    m = km / 1.60934
    mph = (m * 60) * 60
    return mph


def miles_per_hour_to_meters_per_second(x):
    km = x * 1.60934
    m = km * 1000.0
    mps = (m / 60) / 60
    return mps
