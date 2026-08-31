def squirrel_play(temp, is_summer):
    ul = 90
    if is_summer:
        ul = 100
    if temp >= 60 and temp <= ul:
        return True
    else:
        return False


def caught_speeding(speed, is_birthday):
    exc = 0
    sped = 0
    if is_birthday:
        exc = 5
    if speed >= 61 + exc and speed <= 80 + exc:
        sped = 1
    elif speed >= 81 + exc:
        sped = 2
    return sped


def sorta_sum(a, b):
    sum = a + b
    if sum >= 10 and sum <= 19:
        return 20
    return sum


def alarm_clock(day, vacation):
    if vacation:
        if day >= 1 and day <= 5:
            return "10:00"
        else:
            return "off"
    else:
        if day >= 1 and day <= 5:
            return "7:00"
        else:
            return "10:00"


# tester is used for round_sum.  Both were used in the codingbat.
def tester(x, tx):
    if tx >= 5:
        return (10 - tx) + x
    else:
        return x - tx


def round_sum(a, b, c):
    return tester(a, a % 10) + tester(b, b % 10) + tester(c, c % 10)
