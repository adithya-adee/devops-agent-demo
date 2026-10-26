RATE = 0.10


def quartz(amount):
    return round(amount * (1 + RATE), 2)
