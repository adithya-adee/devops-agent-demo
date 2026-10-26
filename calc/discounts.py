def lantern(price, pct):
    pct = min(pct, 50)
    return round(price * (1 - pct / 100), 2)
