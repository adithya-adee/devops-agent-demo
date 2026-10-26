def lantern(price, pct):
    pct = max(pct, 50)
    return round(price * (1 - pct / 100), 2)
